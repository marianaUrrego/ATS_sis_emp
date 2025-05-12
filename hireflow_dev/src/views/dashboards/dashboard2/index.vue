<script setup lang="ts">
import { ref, onMounted } from 'vue';
/* Breadcrumb component */
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';
import UiParentCard from '@/components/shared/UiParentCard.vue';

/*Call Components*/
import TableOffer from '@/components/table/TableOffer.vue';
import RequerimentsCard from '@/components/dashboards/dashboard2/RequerimentsCard.vue';
import RequerimentsCard2 from '@/components/dashboards/dashboard2/RequirementsCardsText.vue';

import { useRoute } from 'vue-router';
const route = useRoute();
const id = route.params.id;

interface Oferta {
    id: string
    nombre: string
    departamento: string
    perfil: string
    habilidades_blandas: string[]
    habilidades_tecnicas: string[]
    titulos: string[]
    experiencia: string[]
}

interface Aplicante {
    nombre_aplicante: string
    correo: string
    id_oferta: string
    oferta: string
    id_estado: string
    estado: string
    cv_url: string
}

const oferta = ref<Oferta | null>(null);
const aplicantes = ref<Aplicante[]>([]);
const isLoadingOferta = ref(false);
const isLoadingAplicantes = ref(false);
const errorOferta = ref<string | null>(null);
const errorAplicantes = ref<string | null>(null);

// template breadcrumb
const page = ref({ title: "" });
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

// Función para cargar la oferta
async function cargarOferta() {
  isLoadingOferta.value = true;
  errorOferta.value = null;
  
  try {
    const response = await fetch(`http://127.0.0.1:8000/ofertas/${id}`);
    if (!response.ok) throw new Error('Error al cargar la oferta');
    
    const data: Oferta = await response.json();
    oferta.value = data;
    
    // Actualizar el título con el nombre de la oferta
    page.value.title = data.nombre;
  } catch (error) {
    console.error('Error al obtener los datos de la oferta:', error);
    errorOferta.value = error instanceof Error ? error.message : 'Error desconocido';
  } finally {
    isLoadingOferta.value = false;
  }
}

// Función para cargar los aplicantes
async function cargarAplicantes() {
  isLoadingAplicantes.value = true;
  errorAplicantes.value = null;
  
  try {
    const response = await fetch(`http://127.0.0.1:8000/ofertas/id/${id}/aplicantes`);
    if (!response.ok) throw new Error('Error al cargar los aplicantes');
    
    const data: Aplicante[] = await response.json();
    aplicantes.value = data;
  } catch (error) {
    console.error('Error al obtener los aplicantes:', error);
    errorAplicantes.value = error instanceof Error ? error.message : 'Error desconocido';
  } finally {
    isLoadingAplicantes.value = false;
  }
}

// Método para abrir CV
function abrirCV(cvUrl: string) {
  window.open(cvUrl, '_blank');
}

onMounted(async () => {
  // Cargar la oferta y los aplicantes al montar el componente
  await cargarOferta();
  await cargarAplicantes();
});
</script>

<template>
    <v-row>
        <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
    </v-row>
    <v-row>
        <v-row class="mb-6">
            <v-col cols="12" class="d-flex align-center justify-space-between">
                <div class="d-flex align-center">
                    <v-col>
                        <h3 class=" display-1 textPrimary font-weight-bold">{{ oferta?.nombre }}</h3>
                    </v-col>
                    <v-col>
                        <v-chip color="success" variant="flat" >{{ oferta?.departamento }}</v-chip>
                    </v-col>
                </div>
                <v-btn color="primary" prepend-icon="mdi-plus" class="text-capitalize">
                Crear nueva oferta
                </v-btn>
            </v-col>
        </v-row>
        
        <v-row class="d-flex align-stretch">
            <!-- Estudios necesarios -->
            <v-col cols="12" md="4">
                <RequerimentsCard class="bg-primary fill-height" :items="oferta.titulos" :nombre-requisito="'Titulos requeridos'"/>
            </v-col>
            <!-- Perfil -->
            <v-col cols="12" md="4">
                <RequerimentsCard2 class="bg-secondary fill-height" :text="oferta.perfil" :nombre-requisito="'Perfil'"/>
            </v-col>
            <!-- Habilidades Blandas -->
            <v-col cols="12" md="4">
                <RequerimentsCard class="bg-error fill-height" :items="oferta.habilidades_blandas" :nombre-requisito="'Habilidades blandas'"/>
            </v-col>
        </v-row>
        
        <!-- Habilidades técnicas -->
        <v-row class="d-flex align-stretch">
            <v-col cols="12" lg="6">
                <RequerimentsCard class="bg-success fill-height" :items="oferta.habilidades_tecnicas" :nombre-requisito="'Habilidades técnicas'"/>
            </v-col>
            <!-- Experiencia necesaria -->
            <v-col cols="12" lg="6">
                <RequerimentsCard class="bg-warning fill-height" :items="oferta.experiencia" :nombre-requisito="'Experiencia necesaria'"/>
            </v-col>
        </v-row>
        
        <!-- Table -->
        <v-row>
            <v-col cols="12">
                <UiParentCard title="Aplicantes a la oferta">
                    <div v-if="isLoadingAplicantes" class="text-center py-5">
                        <v-progress-circular indeterminate color="primary"></v-progress-circular>
                        <p class="mt-3">Cargando aplicantes...</p>
                    </div>
                    <div v-else-if="errorAplicantes" class="text-center text-error py-5">
                        <p>{{ errorAplicantes }}</p>
                        <v-btn color="primary" class="mt-3" @click="cargarAplicantes">Reintentar</v-btn>
                    </div>
                    <div v-else>
                        <TableOffer 
                            :items="aplicantes" 
                            @ver-cv="abrirCV"
                        />
                    </div>
                </UiParentCard>
            </v-col>
        </v-row>
    </template>
</template>