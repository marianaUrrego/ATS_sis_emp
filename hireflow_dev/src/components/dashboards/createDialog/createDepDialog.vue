<script setup lang="ts">
import { ref } from "vue";
import Basic from "@/components/ui-components/alert/Basic.vue";

const dialog = ref(false);
const nombreDepartamento = ref('');

const guardarDepartamento = async () => {
  try {
    const nombre = encodeURIComponent(nombreDepartamento.value);

    const response = await fetch(`http://localhost:8000/ofertas/departamento/${nombre}`, {
      method: 'POST',
    });

    if (!response.ok) {
      const errorText = await response.text(); // para leer el mensaje del servidor si existe
      alert(`Error al guardar el departamento: ${errorText}`);
      return;
    }

    // Éxito
    nombreDepartamento.value = '';
    dialog.value = false;
    alert('Departamento guardado correctamente');
  } catch (error) {
    alert(`Error de red: ${error}`);
    console.error(error);
  }
};
</script>

<template>
  <div class="text-center mt-4 mt-sm-0">
    <v-btn color="primary" class="w-100" flat>
      Crear departamento
      <v-dialog v-model="dialog" activator="parent"  class="dialog-mw">
        <v-card>
            <v-card-title class="pa-5">
                <span class="text-h5">Nuevo departamento</span>
            </v-card-title>
            <v-card-text>
                <v-col>
                    <v-text-field label="nombre del departamento" v-model="nombreDepartamento" required></v-text-field>
                </v-col>
            </v-card-text>
            <v-card-actions>
                <v-btn color="primary"  @click="dialog = false" variant="tonal">Close Dialog</v-btn>
                <v-btn color="success"  @click="guardarDepartamento" variant="tonal" flat>Save</v-btn>
            </v-card-actions>
        </v-card>
      </v-dialog>
    </v-btn>
  </div>
</template>
