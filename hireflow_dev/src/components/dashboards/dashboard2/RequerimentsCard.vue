<script setup lang="ts">
import { ref } from 'vue';
import { string } from 'yup';
defineProps<{
    items : string[]
    nombreRequisito: string
}>()
</script>
<template>
    <v-card elevation="0" class="overflow-hidden">
        <v-card-item class="space-20">
            <div class="d-flex align-center justify-space-between">
                <div>
                    <p class="mb-2 font-weight-semibold text-white text-h4">{{ nombreRequisito }}</p>

                    <div class="d-flex align-center gap-3">
                        
            <v-col >
                <v-row 
                v-for="(item, index) in items"
                :key="index">
                    <h3 class="textPrimary mb-1 opacity-80 mb-1 text-white">{{ item }}</h3> <!--aqui se puede llamar recursivamente los items de la oferta -->
                </v-row>
            </v-col>
                    </div>
                </div>
                <v-avatar size="48" class="rounded-md bg-surface">
                    <h3 class="font-weight-medium textPrimary" height="22">3</h3>
                </v-avatar>
            </div>
        </v-card-item>
    </v-card>
</template>
