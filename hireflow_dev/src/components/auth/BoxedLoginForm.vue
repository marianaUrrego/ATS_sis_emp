<script setup lang="ts">
import { ref } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { Form } from 'vee-validate';

/*Social icons*/
import google from '@/assets/images/svgs/google-icon.svg';
import facebook from '@/assets/images/svgs/facebook-icon.svg';

const checkbox = ref(false);
const valid = ref(false);
const show1 = ref(false);
const password = ref('admin123');
const username = ref('info@wrappixel.com');
const passwordRules = ref([
    (v: string) => !!v || 'Contraseña requerida',
    (v: string) => (v && v.length <= 10) || 'La contraseña debe tener menos de 10 caracteres'
]);
const emailRules = ref([(v: string) => !!v || 'El E-mail es requerido', (v: string) => /.+@.+\..+/.test(v) || 'El E-mail debe ser válido']);

function validate(values: any, { setErrors }: any) {
    const authStore = useAuthStore();
    return authStore.login(username.value, password.value).catch((error) => setErrors({ apiError: error }));
}
</script>

<template>
    <Form @submit="validate" v-slot="{ errors, isSubmitting }" class="mt-5">
        <v-label class="font-weight-semibold pb-2 ">Nombre de usuario</v-label>
        <VTextField v-model="username" :rules="emailRules" class="mb-8" required hide-details="auto"></VTextField>
        <div class="d-flex justify-space-between align-center pb-2">
            <v-label class="font-weight-semibold ">Contraseña</v-label>
            <RouterLink to="/auth/forgot-password2" class="text-primary text-decoration-none font-weight-medium">¿Olvidaste la contraseña ?</RouterLink>
        </div>

        <VTextField v-model="password" :rules="passwordRules" required hide-details="auto" type="password" class="pwdInput"></VTextField>
        <div class="d-flex flex-wrap align-center my-3 ml-n2">
            <v-checkbox
                class="pe-2"
                v-model="checkbox"
                :rules="[(v: any) => !!v || 'Debes aceptar para continuar!']"
                required
                hide-details
                color="primary"
            >
                <template v-slot:label class="font-weight-medium">Mantener sesión iniciada</template>
            </v-checkbox>
        </div>
        <v-btn size="large" :loading="isSubmitting" color="darkgray" :disabled="valid" block type="submit" flat>Iniciar sesión</v-btn>
        <div v-if="errors.apiError" class="mt-2">
            <v-alert color="error">{{ errors.apiError }}</v-alert>
        </div>
    </Form>
</template>
