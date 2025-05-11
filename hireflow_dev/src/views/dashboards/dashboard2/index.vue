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
    <v-row>
        <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
    </v-row>
    <v-row>
        <v-row>
            <v-col cols="12" xl="12" class="py-3 pl-6 pr-4 d-flex align-center mb-5">
                    <v-row>
                        <h3 class="display-1 textPrimary font-weight-bold ">Developer</h3>
                    </v-row>
                    <div class="ml-auto">
                        <v-btn color="primary">
                            <v-icon class="mr-2">mdi-plus</v-icon>Crear nueva oferta
                        </v-btn>
                    </div>
            </v-col>
        </v-row>
        <v-row class="d-flex align-stretch">
            <!-- Estudios necesarios -->
            <v-col cols="12" md="4">
                <RequerimentsCard class="bg-primary fill-height"
                title="Estudios necesarios"
                :data="['estudio1', 'estudio2', 'estudio3']"
                number="3"/>
            </v-col>
            <!-- Perfil -->
            <v-col cols="12" md="4">
                <RequerimentsCard class="bg-secondary fill-height"
                title="Perfil"
                :data="['estudio1', 'estudio2', 'estudio3']"
                number="3"/>
            </v-col>
            <!-- Habilidades Blandas -->
            <v-col cols="12" md="4">
                <RequerimentsCard class="bg-error fill-height"
                title="Habilidades Blandas"
                :data="['estudio1', 'estudio2', 'estudio3']"
                number="3"/>
            </v-col>
            <!-- Habilidades técnicas -->
            <v-col cols="12" lg="6">
                <RequerimentsCard class="bg-success fill-height"
                title="Habilidades técnicas"
                :data="['estudio1', 'estudio2', 'estudio3']"
                number="3"/>
            </v-col>
            <!-- Experiencia necesaria -->
            <v-col cols="12" lg="6">
                <RequerimentsCard class="bg-warning fill-height"
                title="Experiencia necesaria"
                :data="['estudio1', 'estudio3']"
                number="2"/>
            </v-col>
        </v-row>
        <!-- ---------------------------------------------------- -->
        <!-- Table -->
        <!-- ---------------------------------------------------- -->
        <v-row>
            <v-col cols="12">
                <UiParentCard title="Aplicantes a la oferta">
                    <TableOffer/>
                </UiParentCard>
            </v-col>
        </v-row>
        <v-row>
            <DefaultLayout>
                <CardsDashboard />
            </DefaultLayout>
        </v-row>
    </v-row>
</template>
