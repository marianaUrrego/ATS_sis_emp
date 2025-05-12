<script setup lang="ts">
import axios from 'axios'
import { ref, computed, reactive } from 'vue';
import type { PropType } from 'vue';
import { colorVariation } from '@/_mockApis/apps/notes/index';
import FileMultiple from '@/components/forms/form-elements/fileinput/FileInput.vue';
// common components
const dialog = ref(false);
const title = ref('');

const color = ref('primary');
// Definición de la interfaz para los aplicantes
interface Aplicante {
    nombre_aplicante: string
    correo: string
    id_oferta: string
    oferta: string
    id_estado: string
    estado: string
    // Podríamos añadir campos adicionales si tuviéramos más información
}

// Recibir la prop items con la info de los aplicantes
const props = defineProps({
  items: {
    type: Array as PropType<Aplicante[]>,
    default: () => []
  }
});

// Emitir eventos para la página padre
const emit = defineEmits(['recargar-aplicantes']);

const search = ref('');
const estadosSeleccionado = ref('');

// Datos del formulario para nuevo aplicante
const nuevoAplicante = reactive({
  nombre: '',
  correo: '',
  id_oferta: '',
  archivo: null as File | null
});

// Estado para manejar la carga
const isLoading = ref(false);
const errorMessage = ref('');
const successMessage = ref('');

// Extraer estados únicos desde los aplicantes para el selector
const estados = computed(() => {
  if (!props.items || props.items.length === 0) {
    return ['Activo', 'Por Revisar', 'Rechazados', 'Fase de prueba', 'Fase de entrevista', 'Finalistas'];
  }
  
  // Obtener estados únicos de los aplicantes
  const estadosUnicos = [...new Set(props.items.map(item => item.estado))];
  return estadosUnicos.length > 0 ? estadosUnicos : ['Activo', 'Por Revisar', 'Rechazados', 'Fase de prueba', 'Fase de entrevista', 'Finalistas'];
});

// Configuración de encabezados de la tabla
interface Header {
  title: string;
  align: 'start' | 'end' | 'center';
  key: string;
  sortable?: boolean;
  width?: string | number;
}

const headers = ref<Header[]>([
    { title: 'Aplicante', align: 'start', key: 'nombre_aplicante', sortable: true },
    { title: 'Correo', align: 'start', key: 'correo', sortable: true },
    { title: 'Estado', align: 'start', key: 'estado', sortable: true },
    { title: 'Oferta', align: 'end', key: 'oferta', sortable: true },
    { title: 'Acciones', align: 'center', key: 'acciones' },
]);


// Función para determinar el color basado en el estado
function getColor(estado: string) {
    switch(estado.toLowerCase()) {
        case 'activo':
            return '#13DEB9';
        case 'por revisar':
            return '#FFAE1F';
        case 'rechazados':
        case 'rechazado':
            return '#FA896B';
        case 'fase de prueba':
            return '#5D87FF';
        case 'fase de entrevista':
            return '#5D87FF';
        case 'finalistas':
        case 'finalista':
            return '#13DEB9';
        default:
            return '#FFAE1F';
    }
}

const verCV = async (correo: string) => {
    try {
        const response = await axios.get('http://localhost:8000/aplicaciones/cv', {
            params: { correo },
        });

        const urls = response.data;

        if (urls.length > 0) {
            window.open(urls[0], '_blank');
        } else {
            alert('No se encontró el CV para este correo.');
        }
    } catch (error) {
        console.error("No se pudo obtener el CV", error);
        alert("No se pudo obtener el CV del aplicante.");
    }
};

// Función para manejar el cambio de archivo
const handleFileChange = (event: Event) => {
  const input = event.target as HTMLInputElement;
  if (input.files && input.files.length > 0) {
    nuevoAplicante.archivo = input.files[0];
  }
};

// Función para enviar el formulario
const submitForm = async () => {
  // Validar formulario
  if (!nuevoAplicante.nombre.trim()) {
    errorMessage.value = 'El nombre es obligatorio';
    return;
  }
  
  if (!nuevoAplicante.correo.trim()) {
    errorMessage.value = 'El correo es obligatorio';
    return;
  }
  
  if (!nuevoAplicante.id_oferta.trim()) {
    errorMessage.value = 'El ID de la oferta es obligatorio';
    return;
  }
  
  if (!nuevoAplicante.archivo) {
    errorMessage.value = 'Debe seleccionar un archivo PDF de CV';
    return;
  }
  
  isLoading.value = true;
  errorMessage.value = '';
  successMessage.value = '';
  
  try {
    // Crear FormData para enviar archivo
    const formData = new FormData();
    formData.append('nombre', nuevoAplicante.nombre);
    formData.append('correo', nuevoAplicante.correo);
    formData.append('id_oferta', nuevoAplicante.id_oferta);
    formData.append('file', nuevoAplicante.archivo);
    
    // Enviar datos al endpoint
    const response = await axios.post('http://localhost:8000/aplicaciones/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    });
    
    // Mostrar mensaje de éxito
    successMessage.value = 'Aplicante añadido correctamente';
    
    // Limpiar formulario
    nuevoAplicante.nombre = '';
    nuevoAplicante.correo = '';
    nuevoAplicante.archivo = null;
    
    // Emitir evento para recargar aplicantes
    emit('recargar-aplicantes');
    
    // Cerrar diálogo después de un tiempo
    setTimeout(() => {
      dialog.value = false;
      successMessage.value = '';
    }, 2000);
    
  } catch (error) {
    console.error('Error al añadir aplicante:', error);
    errorMessage.value = 'Error al añadir el aplicante. Intente nuevamente.';
  } finally {
    isLoading.value = false;
  }
};

// Establecer valor inicial de id_oferta desde la URL
const setIdOfertaFromRoute = () => {
  const urlParams = new URLSearchParams(window.location.search);
  const id = window.location.pathname.split('/').pop();
  if (id) {
    nuevoAplicante.id_oferta = id;
  }
};

// Llamar a esta función cuando se abra el diálogo
const abrirDialogo = () => {
  dialog.value = true;
  setIdOfertaFromRoute();
};
</script>
<template>
    <v-row>
        <v-col>
            <v-text-field v-model="search" append-inner-icon="mdi-magnify" label="Buscar" single-line hide-details
                class="mb-5" />
        </v-col>

        <v-col>
            <v-select v-model="estadosSeleccionado" :items="estados" label="Estado"></v-select>
        </v-col> 

        <v-col class="text-right align-center">
            <v-btn color="secondary" class="mx-2" variant="outlined" flat @click="abrirDialogo">
                Añadir CVs<v-icon class="mr-2">mdi-plus</v-icon>
            </v-btn>
            
            <v-dialog v-model="dialog" max-width="500">
                <v-card>
                    <v-card-title class="text-h5 py-4">
                        Añadir nuevo aplicante
                    </v-card-title>
                    <v-card-text>
                        <v-alert
                            v-if="errorMessage"
                            type="error"
                            variant="tonal"
                            class="mb-4"
                            closable
                            @click:close="errorMessage = ''"
                        >
                            {{ errorMessage }}
                        </v-alert>
                        
                        <v-alert
                            v-if="successMessage"
                            type="success"
                            variant="tonal"
                            class="mb-4"
                        >
                            {{ successMessage }}
                        </v-alert>
                        
                        <v-form @submit.prevent="submitForm">
                            <v-text-field
                                v-model="nuevoAplicante.nombre"
                                label="Nombre del aplicante"
                                variant="outlined"
                                required
                                class="mb-4"
                            ></v-text-field>
                            
                            <v-text-field
                                v-model="nuevoAplicante.correo"
                                label="Correo electrónico"
                                variant="outlined"
                                type="email"
                                required
                                class="mb-4"
                            ></v-text-field>
                            
                            <v-text-field
                                v-model="nuevoAplicante.id_oferta"
                                label="ID de la oferta"
                                variant="outlined"
                                required
                                class="mb-4"
                            ></v-text-field>
                            
                            <v-file-input
                                label="Seleccionar CV (PDF)"
                                variant="outlined"
                                accept="application/pdf"
                                @change="handleFileChange"
                                required
                                prepend-icon="mdi-file-pdf-box"
                                show-size
                                truncate-length="30"
                            ></v-file-input>
                        </v-form>
                    </v-card-text>
                    <v-card-actions class="pa-4">
                        <v-spacer></v-spacer>
                        <v-btn color="error" variant="tonal" @click="dialog = false" :disabled="isLoading">
                            Cancelar
                        </v-btn>
                        <v-btn color="primary" variant="tonal" @click="submitForm" :loading="isLoading">
                            Guardar
                        </v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
        </v-col>             
    </v-row>
    <v-data-table 
        items-per-page="5" 
        :headers="headers" 
        :items="items"
        :search="search"
        :custom-filter="(value, search, item) => {
            return value !== null &&
                search !== null &&
                typeof value === 'string' &&
                value.toString().toLowerCase().indexOf(search.toLowerCase()) !== -1
        }"
        class="border rounded-md datatabels"
    >
        <template #item.estado="{ item }">
            <v-chip :color="getColor(item.estado)">
                {{ item.estado }}
            </v-chip>
        </template>

        <template #item.acciones="{ item }">
            <v-btn color="primary" size="small" @click="verCV(item.correo)">
                Ver CV
            </v-btn>
        </template>

        <template v-slot:no-data>
            <div class="text-center pa-5">
                No hay aplicantes disponibles
            </div>
        </template>
    </v-data-table>
</template>