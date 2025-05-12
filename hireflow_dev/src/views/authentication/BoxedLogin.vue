<script setup lang="ts">
import BoxedLoginForm from '@/components/auth/BoxedLoginForm.vue';
import Logo from '@/layouts/full/logo/Logo.vue';
import { ref } from 'vue';

import { AuthCuroselData } from '@/_mockApis/components/pages/auth';

/* Login form */
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
                                    <div class="d-flex"><Logo /></div>
                                    <h2 class="text-34 my-6">Vamos a iniciar sesión</h2>
                                    <BoxedLoginForm />
                                    <h6 class="text-16 text-medium-emphasis d-flex align-center mt-6">
                                        ¿No tienes cuenta?
                                        <v-btn
                                            class="pl-0 text-primary text-16 opacity-1 pl-2"
                                            height="auto"
                                            to="/auth/register2"
                                            variant="plain"
                                            >Regístrate</v-btn
                                        >
                                    </h6>
                                </v-col>
                            </v-row>
                        </div>
                    </v-card>
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>
