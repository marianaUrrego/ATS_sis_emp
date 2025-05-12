<script setup lang="ts">
import Logo from '@/layouts/full/logo/Logo.vue';
/* Reset form */
import ResetPassword from '@/components/auth/ResetForm.vue';
import { AuthCuroselData } from '@/_mockApis/components/pages/auth';
</script>

<template>
    <div class="authentication auth-bg">
        <v-container class="pa-3 auth-login">
            <v-row class="h-100vh d-flex justify-center align-center">
                <v-col cols="12" md="8" class="d-flex align-center">
                    <v-card rounded="md" elevation="10" class="mx-auto">
                        <div class="pa-3">
                            <v-row>
                                <v-col cols="12" class="border-e px-md-12 px-6 py-md-12 py-6">
                                    <div class="my-5"><Logo /></div>
                                    <p class="text-body-1 textSecondary">
                                        Ingrese la dirección de correo electrónico asociada a su cuenta y le enviaremos un enlace para restablecer su contraseña.
                                    </p>
                                    <ResetPassword />
                                    <v-btn size="large" color="lightprimary" to="/auth/login2" block class="mt-5 text-primary" flat
                                        >Volver a inicio de sesión</v-btn
                                    >
                                </v-col>
                            </v-row>
                        </div>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>
