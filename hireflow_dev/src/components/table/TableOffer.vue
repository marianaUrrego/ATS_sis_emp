<script setup lang="ts">

import { ref } from 'vue';

//Base de datos simulada
import { BasicDatatables } from '@/_mockApis/components/datatable/dataTable';


const search = ref();
const estadosSeleccionado = ref()
const estado = ref(['Activo', 'Por Revisar', 'Rechazados', 'Fase de prueba', 'Fase de entrevista', 'Finalistas']);
//Esta es la construcción de la tabla, en key toca mirar como traemos los datos reales
const headers : any = ref([
    { title: 'Aplicante', align: 'start', key: 'name' },
    { title: 'Fecha de envío', align: 'start', key: 'project' },
    { title: 'Archivo', align: 'start', key: 'post' },
    { title: 'Estado', align: 'start', key: 'status' },
    { title: 'Oferta', align: 'end', key: 'budget' },
])

/*for status color*/
function getColor(status: string) {
    if (status == 'Active') return '#13DEB9'
    else if (status == 'Cancel') return '#FA896B'
    else if (status == 'Completed') return '#5D87FF'
    else return '#FFAE1F'
}
</script>
<template>
    <v-row>
        <v-col>
            <v-text-field v-model="search" append-inner-icon="mdi-magnify" label="Buscar" single-line hide-details
                class="mb-5" />
        </v-col>

        <v-col>
            <v-select v-model="estadosSeleccionado" :items="estado" label="Estado"></v-select>
        </v-col> 

        <v-col class="text-right align-center">
            <v-btn color="secondary" class="mx-2" variant="outlined" flat>
                Añadir CVs<v-icon class="mr-2">mdi-plus</v-icon>
            </v-btn>
        </v-col>
                        
    </v-row>
    <v-data-table items-per-page="5" :headers="headers" :items="BasicDatatables" :search="search"
        class="border rounded-md datatabels">
            <template v-slot:item.status="{ item }">
                    <v-chip :color="getColor(item.status)">
                        {{ item.status }}
                    </v-chip>
            </template>
    </v-data-table>
</template>