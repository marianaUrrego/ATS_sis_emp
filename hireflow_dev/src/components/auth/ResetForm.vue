<script setup lang="ts">
import { ref } from 'vue';
import Logo from '@/layouts/full/logo/Logo.vue';
const valid = ref(true);
const show1 = ref(false);
const email = ref('');
const emailRules = ref([(v: string) => !!v || 'El E-mail es requerido', (v: string) => /.+@.+\..+/.test(v) || 'El E-mail debe ser válido']);
</script>
<template>
    <v-form ref="form" v-model="valid" lazy-validation action="/dashboards/analytical" class="mt-6">
        <v-label class="font-weight-semibold pb-2">Correo Electrónico</v-label>
        <VTextField v-model="email" :rules="emailRules" required ></VTextField>
        <v-btn size="large" color="darkgray" to="/" block  submit flat>Olvidé la contraseña</v-btn>
    </v-form>
</template>
