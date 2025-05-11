<script setup lang="ts">
import { ref , onMounted} from 'vue';
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
const oferta = ref<Oferta>(
    {
        nombre: "",
        departamento: "",
        perfil: "",
        habilidades_blandas: [],
        habilidades_tecnicas: [],
        titulos: [],
        experiencia: []
    }
)

// template breadcrumb
const page = ref({ title: 'Nombre de la oferta' });
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

onMounted(async () => {
  try {
    // obtener la oferta según el ID
    const response = await fetch(`http://127.0.0.1:8000/ofertas/${id}`)
    if (!response.ok) throw new Error('Error al cargar la oferta')
    const data = await response.json()
    oferta.value = data

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
                    <h3 class="display-1 textPrimary font-weight-bold ">{{ oferta?.nombre }}</h3>
                </v-row>
        </v-col>
        
        <v-row>
            <!-- Estudios necesarios -->
            <v-col cols="12" md="4">
                <RequerimentsCard class="bg-primary" :items="oferta.titulos" :nombre-requisito="'Titulos requeridos'"/>
            </v-col>
            <!-- Perfil -->
            <v-col cols="12" md="4">
                <RequerimentsCard2 class="bg-secondary" :text="oferta.perfil" :nombre-requisito="'Perfil'"/>
            </v-col>
            <!-- Habilidades Blandas -->
            <v-col cols="12" md="4">
                <RequerimentsCard class="bg-error" :items="oferta.habilidades_blandas" :nombre-requisito="'Habilidades blandas'"/>
            </v-col>
        </v-row>
        <!-- Habilidades técnicas -->
        <v-col cols="12" lg="6">
            <RequerimentsCard class="bg-success" :items="oferta.habilidades_tecnicas" :nombre-requisito="'Habilidades técnicas'"/>
        </v-col>
        <!-- Experiencia necesaria -->
        <v-col cols="12" lg="6">
            <RequerimentsCard class="bg-warning" :items="oferta.experiencia" :nombre-requisito="'Experiencia necesaria'"/>
        </v-col>

        <!-- ---------------------------------------------------- -->
        <!-- Table -->
        <!-- ---------------------------------------------------- -->
        <v-col cols="12">
            <UiParentCard title="Aplicantes a la oferta">
                <TableOffer/>
            </UiParentCard>
        </v-col>
        <DefaultLayout>
            <CardsDashboard />
        </DefaultLayout>
    </v-row>
</template>
