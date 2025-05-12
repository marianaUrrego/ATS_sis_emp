<script setup lang="ts">
import { ref, computed } from 'vue';
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
import { useNoteStore } from '@/stores/apps/notes';
import { colorVariation } from '@/_mockApis/apps/notes/index';

const store = useNoteStore();
const getNote = computed(() => {
    return store.notes[store.notesContent - 1];
});
const locations = ref(['Finanzas', 'Marketing', 'RRHH', 'Desarrollo']);
const location = ref();

const hab_blandas = ref(['Comunicación', 'Trabajo en equipo']);
const hab_blanda = ref();


const hab_tecnicas = ref(['Java', 'SQL']);
const hab_tecnica = ref();


const estudios = ref(['Pre grado', 'Especialización']);
const estudio = ref();
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
                        <v-select v-model="estudio" :items="estudios" label="Seleccionar área"></v-select>
                    </UiChildCard>
                </v-col>
                <v-col cols="12" sm="12" lg="6">
                    <UiChildCard title="Habilidades blandas">
                        <v-select v-model="hab_blanda" :items="hab_blandas" label="Seleccionar área"></v-select>
                    </UiChildCard>
                </v-col>
                <v-col cols="12" sm="12" lg="6">
                    <UiChildCard title="Habilidades técnicas">
                        <v-select v-model="hab_tecnica" :items="hab_tecnicas" label="Seleccionar área"></v-select>
                    </UiChildCard>
                </v-col>
                <v-col cols="12" sm="12" lg="6">
                    <UiChildCard title="Experiencia necesaria">
                        <v-select v-model="location" :items="locations" label="Seleccionar área"></v-select>
                    </UiChildCard>
                </v-col>
            </v-row>    
        </UiParentCard>
        <v-sheet v-if="getNote">
            <v-sheet class="pa-6">
                <h4 class="text-h6 mb-4">Change Title</h4>
                <v-textarea outlined name="Note" v-model="getNote.title"></v-textarea>

                <h4 class="text-h6 mt-4 mb-4">Change Notes Color</h4>
                <div class="d-flex gap-3 align-center">
                    <v-btn
                        icon
                        v-for="btcolor in colorVariation"
                        :key="btcolor.id"
                        size="x-small"
                        :color="btcolor.color"
                        @click="store.updateNote(getNote.id, btcolor.color)"
                    >
                        <CheckIcon width="16" v-if="getNote.color === btcolor.color" />
                    </v-btn>
                </div>
            </v-sheet>
        </v-sheet>
    </v-row>
</template>

