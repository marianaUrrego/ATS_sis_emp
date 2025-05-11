<script setup lang="ts">
<<<<<<< HEAD
import { number, string } from 'yup';


/* Props */
const { title, data } = defineProps({
  title: String,
  data: Array,
  number: String
})

=======
import { ref } from 'vue';
import { string } from 'yup';
defineProps<{
    items : string[]
    nombreRequisito: string
}>()
>>>>>>> ef51bc2a9441af4a711d01cb9bf0ecf15ad5aff7
</script>
<template>
    <v-card elevation="0" class="overflow-hidden">
        <v-card-item class="space-20">
            <div class="d-flex align-center justify-space-between">
                <div>
<<<<<<< HEAD
                    <p class="mb-2 font-weight-semibold text-white text-h4">{{ title }}</p>

                    <div class="d-flex align-center gap-3">
                        
            <v-row >
                <v-col>
                    <div>
                        <h3
                        v-for="(item, index) in data"
                        :key="index"
                        class="textPrimary mb-1 opacity-80 text-white"
                        >
                        {{ item }}
                        </h3>
                    </div>    
                </v-col>
            </v-row>
=======
                    <p class="mb-2 font-weight-semibold text-white text-h4">{{ nombreRequisito }}</p>

                    <div class="d-flex align-center gap-3">
                        
            <v-col >
                <v-row 
                v-for="(item, index) in items"
                :key="index">
                    <h3 class="textPrimary mb-1 opacity-80 mb-1 text-white">{{ item }}</h3> <!--aqui se puede llamar recursivamente los items de la oferta -->
                </v-row>
            </v-col>
>>>>>>> ef51bc2a9441af4a711d01cb9bf0ecf15ad5aff7
                    </div>
                </div>
                <v-avatar size="48" class="rounded-md bg-surface">
                    <h3 class="font-weight-medium textPrimary" height="22">3</h3>
                </v-avatar>
            </div>
        </v-card-item>
    </v-card>
</template>
