<script setup lang="ts">
import { ref, onMounted } from 'vue';
/* Breadcrumb component */
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';

import UiParentCard from '@/components/shared/UiParentCard.vue';

/*Call Components*/
import CardsDashboard from '@/components/dashboards/dashboard2/CardsDashboard.vue';
import TableOffer from '@/components/table/TableOffer.vue';
import RequerimentsCard from '@/components/dashboards/dashboard2/RequerimentsCard.vue';
import RequerimentsCard2 from '@/components/dashboards/dashboard2/RequirementsCardsText.vue';

import { useRoute } from 'vue-router';
const route = useRoute();
const id = route.params.id;

interface Oferta {
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
}

// Datos de oferta simulados para pruebas
const ofertaSimulada = {
    nombre: "Analista de Finanzas",
    departamento: "Finanzas",
    perfil: "Profesional en finanzas con experiencia en análisis financiero y capacidad para interpretar datos y generar reportes estratégicos. Se valorará conocimiento en herramientas de Business Intelligence.",
    habilidades_blandas: ["Trabajo en equipo", "Comunicación efectiva", "Resolución de problemas", "Adaptabilidad"],
    habilidades_tecnicas: ["Excel avanzado", "Power BI", "SAP FI", "Análisis de datos", "Forecasting financiero"],
    titulos: ["Licenciatura en Finanzas", "Economía", "Contabilidad", "MBA (deseable)"],
    experiencia: ["3+ años en análisis financiero", "Experiencia en reportería", "Conocimiento de indicadores KPI"]
};

// Datos simulados de 2 aplicantes
const aplicantesMock: Aplicante[] = [
  {
    nombre_aplicante: "Ana García Rodríguez",
    correo: "ana.garcia@ejemplo.com",
    id_oferta: "550e8400-e29b-41d4-a716-446655440000",
    oferta: "Analista de Finanzas",
    id_estado: "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    estado: "Activo"
  },
  {
    nombre_aplicante: "Carlos Martínez López",
    correo: "carlos.martinez@ejemplo.com",
    id_oferta: "550e8400-e29b-41d4-a716-446655440000",
    oferta: "Analista de Finanzas",
    id_estado: "b2c3d4e5-f6a7-8901-bcde-f12345678901",
    estado: "Por Revisar"
  }
];

const oferta = ref<Oferta>(ofertaSimulada);
const aplicantes = ref<Aplicante[]>([]);
const isLoadingAplicantes = ref(false);
const errorAplicantes = ref<string | null>(null);

// template breadcrumb
const page = ref({ title: ofertaSimulada.nombre });
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

// Función para cargar la oferta (aquí usamos datos simulados)
async function cargarOferta() {
  try {
    // En un entorno real, aquí harías la llamada fetch
    // const response = await fetch(`http://127.0.0.1:8000/ofertas/${id}`);
    // if (!response.ok) throw new Error('Error al cargar la oferta');
    // const data = await response.json();
    // oferta.value = data;
    
    // Simulamos con datos estáticos
    oferta.value = ofertaSimulada;
    
    // Actualizar el título con el nombre de la oferta
    page.value.title = oferta.value.nombre;
  } catch (error) {
    console.error('Error al obtener los datos de la oferta:', error);
  }
}

// Función para cargar los aplicantes (simulada)
async function cargarAplicantes() {
  isLoadingAplicantes.value = true;
  errorAplicantes.value = null;
  
  try {
    // En un entorno real:
    // const response = await fetch(`http://127.0.0.1:8000/id/${id}/aplicantes`);
    // if (!response.ok) throw new Error('Error al cargar los aplicantes');
    // const data = await response.json();
    // aplicantes.value = data;
    
    // Simulamos la carga con un breve retraso
    await new Promise(resolve => setTimeout(resolve, 800));
    aplicantes.value = aplicantesMock;
  } catch (error) {
    console.error('Error al obtener los aplicantes:', error);
    errorAplicantes.value = error instanceof Error ? error.message : 'Error desconocido';
  } finally {
    isLoadingAplicantes.value = false;
  }
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
        <v-row>
            <v-col cols="12" xl="5" class="py-3 pl-6 pr-4 d-flex align-center mb-5">
                    <v-row>
                        <h3 class="display-1 textPrimary font-weight-bold ">{{ oferta?.nombre }}</h3>
                    </v-row>
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

        <!-- ---------------------------------------------------- -->
        <!-- Table -->
        <!-- ---------------------------------------------------- -->
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
                        <TableOffer :items="aplicantes" />
                    </div>
                </UiParentCard>
            </v-col>
        </v-row>
    </v-row>
</template>