<script setup lang="ts">
import { ref, computed, onMounted } from 'vue';
/* Breadcrumb component */
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';
import UiChildCard from '@/components/shared/UiChildCard.vue';
import { useNoteStore } from '@/stores/apps/notes';
import CreateDepDialog from '@/components/dashboards/createDialog/createDepDialog.vue';

// template breadcrumb
const page = ref({ title: 'crear oferta' });
const breadcrumbs = ref([
    {
        text: 'Home',
        disabled: false,
        href: '#'
    },
    {
        text: 'Oferta',
        disabled: true,
        href: '#'
    }
]);

const store = useNoteStore();
const getNote = computed(() => {
    return store.notes[store.notesContent - 1];
});

/*inputs*/
const nameOffer = ref('input para el nombre de la oferta');

const departamentos = ref<Array<{ id: number; nombre: string }>>([]);
const depaSeleccionado = ref<string | null>(null);

const hab_blandas = ref<string[]>([]);
const nuevaHab_blanda = ref('');


const hab_tecnicas = ref<string[]>([]);
const nuevaHab_tecnica = ref("");

const nuevoEstudio = ref('');
const estudios = ref<string[]>([]);

const experiencia = ref<string[]>([]);
const nuevaExp = ref("")

const agregarEstudio = () => {
  const item = nuevoEstudio.value.trim();
  if (item !== '') {
    estudios.value.push(item);
    nuevoEstudio.value = '';
  }
};

const eliminarEstudio = (index: number) => {
  estudios.value.splice(index, 1);
};

const agregarHabBlandas = () => {
  const item = nuevaHab_blanda.value.trim();
  if (item !== '') {
    hab_blandas.value.push(item);
    nuevaHab_blanda.value = '';
  }
};

const eliminarHabBlanda = (index: number) => {
  hab_blandas.value.splice(index, 1);
};

const agregarHabTecnicas = () => {
  const item = nuevaHab_tecnica.value.trim();
  if (item !== '') {
    hab_tecnicas.value.push(item);
    nuevaHab_tecnica.value = '';
  }
};

const eliminarHabTecnica = (index: number) => {
  hab_tecnicas.value.splice(index, 1);
};

const agregarExperiencia = () => {
    const item = nuevaExp.value.trim();
  if (item !== '') {
    experiencia.value.push(item);
    nuevaExp.value = '';
  }
}

const eliminarExperiencia = (index: number) => {
  experiencia.value.splice(index, 1);
};


const perfil = ref()

const enviarDatos = () => {
  const payload = {
    nombre: nameOffer.value,
    departamento: depaSeleccionado.value,
    perfil: perfil.value,
    habilidades_blandas: hab_blandas.value,
    habilidades_tecnicas: hab_tecnicas.value,
    titulos: estudios.value,
    experiencia: experiencia.value,
  };

  // Aquí puedes realizar la llamada a tu API utilizando fetch o alguna otra librería como Axios
  console.log('Datos a enviar:', JSON.stringify(payload, null, 2));

  // Ejemplo de cómo podrías hacer la llamada con fetch:
  fetch(`http://127.0.0.1:8000/ofertas/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  })
    .then(response => response.json())
    .then(data => {
      console.log('Respuesta de la API:', data);
      // Manejar la respuesta de la API aquí
      if(data[0] = "oferta creada exitosamente" ){
        alert( data[0])
      }
    })
    .catch(error => {
      console.error('Error al enviar los datos:', error);
      alert("la oferta no se creo de forma exitosa:"+ error)
      // Manejar errores aquí
    });
};

onMounted(async () => {
  try {
     // Obtener los departamentos
    const resDepartamentos = await fetch('http://127.0.0.1:8000/ofertas/departamentos/')
    if (!resDepartamentos.ok) throw new Error('Error al cargar departamentos')
    const dataDepartamentos = await resDepartamentos.json()
    departamentos.value = dataDepartamentos

  } catch (error) {
    console.error('Error al obtener los datos:', error)
  }
})
</script>
<template>
    <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
    <v-row>
        <v-col cols="12" xl="5" class="py-3 pl-6 pr-4 d-flex align-center mb-5">
                <v-row>
                    <h3 class="display-1 textPrimary font-weight-bold ">Crear oferta</h3>
                </v-row>
        </v-col>
        <v-col cols="12">
                <v-card  variant="outlined">
                    <v-card-item>
                        <div class="mt-5">
                            <v-row>
                                <v-col cols="12" md="6">
                                     <v-label class="mb-2 font-weight-medium">Nombre oferta</v-label>
                                        <v-text-field
                                            color="primary"
                                            variant="outlined"
                                            type="text"
                                            v-model="nameOffer"
                                            hide-details
                                        />
                                </v-col>
                            </v-row>
                            <v-row>
                                <v-col cols="12" md="6">
                                    <div class="mt-4">
                                        <v-label class="mb-2 font-weight-medium">Nombre departamento</v-label>
                                        <v-row>
                                            <v-col cols="12" md="6">
                                                <v-select v-model="depaSeleccionado" :items="departamentos" item-title="nombre" item-value="nombre" label="Seleccionar departamento"></v-select>
                                            </v-col>
                                            <v-col cols="12" md="auto" class="text-right">
                                                <CreateDepDialog />
                                            </v-col>
                                        </v-row>
                                    </div>
                                </v-col>
                            </v-row>
                            <v-col>
                                    <v-sheet>
                                        <v-label class="mb-2 font-weight-medium">Perfil</v-label>
                                        <v-textarea outlined name="Note" v-model="perfil"></v-textarea>
                                    </v-sheet>
                            </v-col>
                        </div>
                    </v-card-item>
                </v-card>
            </v-col>
        
        <UiParentCard title="Descripción detallada de la oferta">
            <v-row>
                <v-col cols="12" sm="12" lg="6">
                    <UiChildCard title="Estudios necesarios">
                        <v-text-field
                        label="Agregar item"
                        v-model="nuevoEstudio"
                        @keyup.enter="agregarEstudio()"
                        append-inner-icon="mdi-plus"
                        @click:append-inner="agregarEstudio()"
                        ></v-text-field>
                        <v-list v-if="estudios.length">
                            <v-list-item
                                v-for="(item, index) in estudios"
                                :key="index"
                            >
                                <v-row>
                                    <v-col>
                                        <v-list-item-title>{{ item }}</v-list-item-title>
                                    </v-col>
                                    <v-col>
                                        <v-btn icon color="error" density="compact" @click="eliminarEstudio(index)">
                                            <v-icon>mdi-delete</v-icon>
                                        </v-btn>
                                    </v-col>
                                </v-row>
                            </v-list-item>
                        </v-list>
                    </UiChildCard>
                </v-col>
                <v-col cols="12" sm="12" lg="6">
                    <UiChildCard title="Habilidades blandas">
                        <v-text-field
                        label="Agregar item"
                        v-model="nuevaHab_blanda"
                        @keyup.enter="agregarHabBlandas()"
                        append-inner-icon="mdi-plus"
                        @click:append-inner="agregarHabBlandas()"
                        ></v-text-field>
                        <v-list v-if="hab_blandas.length">
                            <v-list-item
                                v-for="(item, index) in hab_blandas"
                                :key="index"
                            >
                                <v-row>
                                    <v-col>
                                        <v-list-item-title>{{ item }}</v-list-item-title>
                                    </v-col>
                                    <v-col>
                                        <v-btn icon color="error" density="compact" @click="eliminarHabBlanda(index)">
                                            <v-icon>mdi-delete</v-icon>
                                        </v-btn>
                                    </v-col>
                                </v-row>
                            </v-list-item>
                        </v-list>
                    </UiChildCard>
                </v-col>
                <v-col cols="12" sm="12" lg="6">
                    <UiChildCard title="Habilidades técnicas">
                        <v-text-field
                        label="Agregar item"
                        v-model="nuevaHab_tecnica"
                        @keyup.enter="agregarHabTecnicas()"
                        append-inner-icon="mdi-plus"
                        @click:append-inner="agregarHabTecnicas()"
                        ></v-text-field>
                        <v-list v-if="hab_tecnicas.length">
                            <v-list-item
                                v-for="(item, index) in hab_tecnicas"
                                :key="index"
                            >
                                <v-row>
                                    <v-col>
                                        <v-list-item-title>{{ item }}</v-list-item-title>
                                    </v-col>
                                    <v-col>
                                        <v-btn icon color="error" density="compact" @click="eliminarHabTecnica(index)">
                                            <v-icon>mdi-delete</v-icon>
                                        </v-btn>
                                    </v-col>
                                </v-row>
                            </v-list-item>
                        </v-list>
                    </UiChildCard>
                </v-col>
                <v-col cols="12" sm="12" lg="6">
                    <UiChildCard title="Experiencia necesaria">
                        <v-text-field
                        label="Agregar item"
                        v-model="nuevaExp"
                        @keyup.enter="agregarExperiencia()"
                        append-inner-icon="mdi-plus"
                        @click:append-inner="agregarExperiencia()"
                        ></v-text-field>
                        <v-list v-if="experiencia.length">
                            <v-list-item
                                v-for="(item, index) in experiencia"
                                :key="index"
                            >
                                <v-row>
                                    <v-col>
                                        <v-list-item-title>{{ item }}</v-list-item-title>
                                    </v-col>
                                    <v-col>
                                        <v-btn icon color="error" density="compact" @click="eliminarExperiencia(index)">
                                            <v-icon>mdi-delete</v-icon>
                                        </v-btn>
                                    </v-col>
                                </v-row>
                            </v-list-item>
                        </v-list>
                    </UiChildCard>
                </v-col>
            </v-row>    
        </UiParentCard>
        <v-btn style="margin-top: 20px;" color="primary" class="w-100" flat @click="enviarDatos()">Crear oferta</v-btn>
        
    </v-row>
</template>
