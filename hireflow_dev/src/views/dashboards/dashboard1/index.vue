<script setup lang="ts">
/*Call Components*/

</script>
<template>
    <!--cuando pongamos info lo podemos hacer modular, como los componentes son tan chiquitos lo hice así por ahora-->
    <v-row>
        <v-col cols="12" xl="5" class="py-3 pl-6 pr-4 d-flex align-center mb-5">
                <v-row>
                    <h3 class="display-1 textPrimary font-weight-bold ">Home</h3>
                </v-row>
        </v-col>
        <v-col cols="10" md="6">
                <div class="bg-lightprimary pa-7 rounded-md">
                    <h2 class="text-primary text-24">Ofertas activas</h2>
                    <h6 class="text-primary text-h1">28</h6>
                </div>
        </v-col>
        <v-col cols="10" md="6">
                <div class="bg-lightsecondary pa-7 rounded-md">
                    <h2 class="text-secondary text-24">Ofertas activas</h2>
                    <h6 class="text-secondary text-h1">28</h6>
                </div>
        </v-col>
        <v-row>
        <v-col cols="12">
            <v-card variant="outlined">
                <v-card-item>
                    <h4 class="text-h4 text-center ">Últimos aplicantes</h4>
                    <v-row >
                        <v-col>
                            <div class="d-flex gap-3 mb-5">
                                <span class="text-h6">Sir, P P Institute Of Science</span>
                            </div>
                            <div class="d-flex gap-3 mb-5">
                                <span class="text-h6">xyzjonathan@gmail.com</span>
                            </div>
                        </v-col>

                        <v-col>
                            <div class="d-flex gap-3 mb-5">
                                <span class="text-h6 textSecondary">www.xyz.com</span>
                            </div>
                            <div class="d-flex gap-3 mb-5">
                                <p class="text-h6 textSecondary">Newyork, USA - 100001</p>
                            </div>
                        </v-col>
                    </v-row>
                </v-card-item>
            </v-card>
        </v-col>
    </v-row>
    </v-row>
</template>
