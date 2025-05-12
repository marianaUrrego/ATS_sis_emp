<script setup lang="ts">
import { ref, computed } from 'vue';
import type { PropType } from 'vue';
import { colorVariation } from '@/_mockApis/apps/notes/index';
import FileMultiple from '@/components/forms/form-elements/fileinput/FileInput.vue';
// common components
const dialog = ref(false);
const title = ref('');

const color = ref('primary');
function addNote() {
    return (
        getNote.value.push({ id: getId + 1, title: title.value, color: color.value, datef: new Date() }),
        (dialog.value = false),
        (title.value = '')
    );
}
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

const search = ref('');
const estadosSeleccionado = ref('');

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
            <v-btn color="secondary" class="mx-2" variant="outlined" flat @click="dialog= true">
                Añadir CVs<v-icon class="mr-2">mdi-plus</v-icon>
            </v-btn>
            
            <v-dialog v-model="dialog" max-width="500">
                <v-card>
                    <v-card-text>
                        <h4 class="text-h6 mb-4">Cargar archivos</h4>
                        <UiChildCard title="Multiple">
                                <FileMultiple />
                        </UiChildCard>
                    </v-card-text>
                    <v-card-actions>
                        <v-btn color="primary" variant="tonal" @click="addNote">Guardar</v-btn>
                        <v-btn color="error" variant="tonal" @click="dialog = false">Cerrar pestaña</v-btn>
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
        <template v-slot:item.estado="{ item }">
            <v-chip :color="getColor(item.estado)">
                {{ item.estado }}
            </v-chip>
        </template>
        
        <!-- Si no hay items, mostrar mensaje -->
        <template v-slot:no-data>
            <div class="text-center pa-5">
                No hay aplicantes disponibles
            </div>
        </template>
    </v-data-table>
</template>