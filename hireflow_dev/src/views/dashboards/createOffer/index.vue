<script setup lang="ts">
import { ref } from 'vue';
/* Breadcrumb component */
import BaseBreadcrumb from '@/components/shared/BaseBreadcrumb.vue';

import UiParentCard from '@/components/shared/UiParentCard.vue';

import UiChildCard from '@/components/shared/UiChildCard.vue';
/*Call Components*/
import CardsDashboard from '@/components/dashboards/dashboard2/CardsDashboard.vue';
import TableOffer from '@/components/table/TableOffer.vue';

/*inputs*/
const nameOffer = ref('input para el nombre de la oferta');
// template breadcrumb
const page = ref({ title: '' });
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

const locations = ref(['Finanzas', 'Marketing', 'RRHH', 'Desarrollo']);
const location = ref();
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
                                        <v-select v-model="location" :items="locations" label="Seleccionar departamento"></v-select>
                                    </div>
                                </v-col>
                            </v-row>
                        </div>
                    </v-card-item>
                </v-card>
            </v-col>
        
        <UiParentCard title="Descripción resumida de la oferta">
            <v-row>
                <v-col cols="12" sm="12" lg="6">
                    <UiChildCard title="Estudios necesarios">
                        <v-select v-model="location" :items="locations" label="Seleccionar área"></v-select> <!--puede ser un dropdown o un input-->
                    </UiChildCard>
                </v-col>
                <v-col cols="12" sm="12" lg="6">
                    <UiChildCard title="Habilidades blandas">
                        <v-select v-model="location" :items="locations" label="Seleccionar área"></v-select> <!--puede ser un dropdown o un input-->
                    </UiChildCard>
                </v-col>
                <v-col cols="12" sm="12" lg="6">
                    <UiChildCard title="Habilidades técnicas">
                        <v-select v-model="location" :items="locations" label="Seleccionar área"></v-select> <!--puede ser un dropdown o un input-->
                    </UiChildCard>
                </v-col>
                <v-col cols="12" sm="12" lg="6">
                    <UiChildCard title="Experiencia necesaria">
                        <v-select v-model="location" :items="locations" label="Seleccionar área"></v-select> <!--puede ser un dropdown o un input-->
                    </UiChildCard>
                </v-col>
            </v-row>    
        </UiParentCard> 
    </v-row>
</template>
