<script setup lang="ts">
defineProps<{
    text: string
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
                        
            <v-row >
                <v-col>
                    <p class="textPrimary mb-1 text-white">{{ text }}</p>   
                </v-col>
            </v-row>
                    </div>
                </div>
            </div>
        </v-card-item>
    </v-card>
</template>