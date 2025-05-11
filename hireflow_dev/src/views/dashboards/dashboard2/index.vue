<script setup lang="ts">
import { ref } from 'vue';
/* Breadcrumb component */
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';

import UiParentCard from '@/components/shared/UiParentCard.vue';

/*Call Components*/
import CardsDashboard from '@/components/dashboards/dashboard2/CardsDashboard.vue';
import TableOffer from '@/components/table/TableOffer.vue';
import RequerimentsCard from '@/components/dashboards/dashboard2/RequerimentsCard.vue';
import RequerimentsCard2 from '@/components/dashboards/dashboard2/RequirementsCardsText.vue';
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

</script>
<template>
    <BaseBreadcrumb :title="page.title" :breadcrumbs="breadcrumbs"></BaseBreadcrumb>
    <v-row>
        <v-col cols="12" xl="5" class="py-3 pl-6 pr-4 d-flex align-center mb-5">
                <v-row>
                    <h3 class="display-1 textPrimary font-weight-bold ">Developer</h3>
                </v-row>
                <div class="ml-auto">
                    <v-btn color="primary">
                        <v-icon class="mr-2">mdi-plus</v-icon>Crear nueva oferta
                    </v-btn>
                </div>
        </v-col>
        
        <v-row>
            <!-- Estudios necesarios -->
            <v-col cols="12" md="4">
                <RequerimentsCard class="bg-primary"/>
            </v-col>
            <!-- Perfil -->
            <v-col cols="12" md="4">
                <RequerimentsCard2 class="bg-secondary"/>
            </v-col>
            <!-- Habilidades Blandas -->
            <v-col cols="12" md="4">
                <RequerimentsCard class="bg-error"/>
            </v-col>
        </v-row>
        <!-- Habilidades técnicas -->
        <v-col cols="12" lg="6">
            <RequerimentsCard class="bg-success"/>
        </v-col>
        <!-- Experiencia necesaria -->
        <v-col cols="12" lg="6">
            <RequerimentsCard2 class="bg-warning"/>
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
