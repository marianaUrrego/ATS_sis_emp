<script setup lang="ts">
</script>
<template>
    <v-card elevation="0" class="overflow-hidden">
        <v-card-item class="space-20">
            <div class="d-flex align-center justify-space-between">
                <div>
                    <p class="mb-2 font-weight-semibold text-white text-h4">Estudios</p>

                    <div class="d-flex align-center gap-3">
                        
            <v-row >
                <v-col>
                    <h3 class="textPrimary mb-1 opacity-80 mb-1 text-white">Pregrado</h3> <!--aqui se puede llamar recursivamente los items de la oferta -->
                    <h3 class="textPrimary mb-1 opacity-80 mb-1 text-white">Especialización</h3>     
                </v-col>
            </v-row>
                    </div>
                </div>
                <v-avatar size="48" class="rounded-md bg-surface">
                    <h3 class="font-weight-medium textPrimary" height="22">3</h3>
                </v-avatar>
            </div>
        </v-card-item>
    </v-card>
</template>
