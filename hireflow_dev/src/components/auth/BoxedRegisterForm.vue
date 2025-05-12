<script setup lang="ts">
import { ref } from 'vue';
import Logo from '@/layouts/full/logo/Logo.vue';
/*Social icons*/
import google from '@/assets/images/svgs/google-icon.svg';
import facebook from '@/assets/images/svgs/facebook-icon.svg';

const checkbox = ref(false);
const valid = ref(true);
const show1 = ref(false);
const password = ref('');
const email = ref('');
const passwordRules = ref([
    (v: string) => !!v || 'Contraseña requerida',
    (v: string) => (v && v.length <= 10) || 'La contraseña debe tener menos de 10 caracteres'
]);
const emailRules = ref([(v: string) => !!v || 'El E-mail es requerido', (v: string) => /.+@.+\..+/.test(v) || 'El E-mail debe ser válido']);
const fname = ref('');
const fnameRules = ref([
    (v: string) => !!v || 'Nombre requerido',
    (v: string) => (v && v.length <= 10) || 'El nombre debe tener menos de 10 caracteres'
]);
</script>
<template>
    <v-form ref="form" v-model="valid" lazy-validation action="/pages/boxedlogin" class="mt-5">
        <v-label class="font-weight-medium pb-2">Nombre</v-label>
        <VTextField v-model="fname" :rules="fnameRules" required ></VTextField>
        <v-label class="font-weight-medium pb-2">Corre Electrónico</v-label>
        <VTextField v-model="email" :rules="emailRules" required ></VTextField>
        <v-label class="font-weight-medium pb-2">Contraseña</v-label>
        <VTextField
            v-model="password"
            :counter="10"
            :rules="passwordRules"
            required
            variant="outlined"
            type="password"
            color="primary"
        ></VTextField>
        <v-btn size="large" class="mt-2" color="darkgray" block submit flat>Registrarse</v-btn>
    </v-form>
</template>
