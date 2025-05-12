<script setup lang="ts">
import Logo from '@/layouts/full/logo/Logo.vue';
/* Register form */
import BoxedRegisterForm from '@/components/auth/BoxedRegisterForm.vue';
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
                                <v-col cols="12"  class="border-e px-md-12 px-6 py-md-12 py-6">
                                    <div class="d-flex"><Logo /></div>
                                    <h2 class="text-34 my-6">Vamos a registrarte</h2>
                                    <BoxedRegisterForm/>
                                    <h6 class="text-16 text-medium-emphasis d-flex align-center mt-6">
                                        ¿Ya tienes una cuenta?
                                        <v-btn variant="plain" to="/auth/login2" class="pl-0 text-primary text-16 opacity-1 pl-2"
                                            >
                                        Inicia sesión ahora</v-btn
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
