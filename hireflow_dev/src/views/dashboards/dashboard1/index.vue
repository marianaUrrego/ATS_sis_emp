<script setup lang="ts">
/*Call Components*/
import RequerimentsCard from '@/components/dashboards/dashboard2/RequerimentsCard.vue';
</script>
<template>
    <!--cuando pongamos info lo podemos hacer modular, como los componentes son tan chiquitos lo hice así por ahora-->
    <v-row>
        <v-col cols="12" xl="12" class="py-3 pl-6 pr-4 d-flex align-center mb-5">
                <v-row>
                    <h3 class="display-1 textPrimary font-weight-bold ">Home</h3>
                </v-row>
        </v-col>
        <v-col cols="12" md="6">
                <div class="bg-lightprimary pa-7 rounded-md">
                    <h2 class="text-primary text-24">Ofertas activas</h2>
                    <h6 class="text-primary text-h1">28</h6>
                </div>
        </v-col>
        <v-col cols="12" md="6">
                <div class="bg-lightsecondary pa-7 rounded-md">
                    <h2 class="text-secondary text-24">Ofertas activas</h2>
                    <h6 class="text-secondary text-h1">28</h6>
                </div>
        </v-col>

        <v-col cols="12">
            <v-card variant="outlined" class="px-6 py-6">
                <h4 class="text-h4 text-center mt-1 mb-6">Últimos aplicantes</h4>
                    <div class="d-flex flex-column px-4" style="width: 100%;">
                        <div class="d-flex gap-3 mb-5" style="justify-content: space-between;">
                            <span class="text-h6">Alfonso Gabriel Jiménez Rivas, Desarrollador de software Front end</span>
                            <span class="text-h6" style="color: #7F7F7F;">Hoy</span>
                        </div>
                        <div class="d-flex gap-3 mb-5" style="justify-content: space-between;">
                            <span class="text-h6">Juana Jaramillo Montoya, Administrador de bases de datos no rel...</span>
                            <span class="text-h6" style="color: #7F7F7F;">Ayer</span>
                        </div>
                        <div class="d-flex gap-3 mb-5" style="justify-content: space-between;">
                            <span class="text-h6">Juanita Correa Salazar, Administrador de bases de datos no relac...</span>
                            <span class="text-h6" style="color: #7F7F7F;">Hace 2 días</span>
                        </div>
                    </div>
            </v-card>
        </v-col>
    </v-row>
</template>