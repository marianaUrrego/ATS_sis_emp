<script setup lang="ts">
    defineProps<{
    nombreOferta: string
    departamento: string
    fechaCreacion: string
    }>()
</script>
<template>
    <v-row>
        <v-col cols="12">
            <v-card variant="outlined">
                <v-card-item>
                    <h4 class="text-h4" style="margin-bottom: 20px;">{{ nombreOferta }}</h4>
                    <div class="d-flex gap-3 mb-5">
                        <span class="text-h6">departamento</span>
                        <p>{{ departamento }}</p>
                    </div>
                    <div class="d-flex gap-3 mb-5">
                        <span class="text-h6">fecha de creación</span>
                        <p>{{ fechaCreacion }}</p>
                    </div>
                </v-card-item>
            </v-card>
        </v-col>
    </v-row>
</template>
