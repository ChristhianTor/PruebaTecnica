<template>
    <div class="container">
      <h2>{{ isEditing ? 'Editar Producto' : 'Agregar Producto' }}</h2>
      <form @submit.prevent="saveProduct">
        <div class="form-group">
          <label for="name">Nombre</label>
          <input type="text" v-model="product.name" class="form-control" id="name" required>
        </div>
        <div class="form-group">
          <label for="price">Precio</label>
          <input type="number" v-model="product.price" class="form-control" id="price" required>
        </div>
        <button type="submit" class="btn btn-primary">{{ isEditing ? 'Actualizar' : 'Guardar' }}</button>
        <button type="button" class="btn btn-secondary" @click="cancelEdit">Cancelar</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        product: {
          name: '',
          price: null
        },
        isEditing: false,
        productId: null
      };
    },
    methods: {
      async saveProduct() {
        const method = this.isEditing ? 'PUT' : 'POST';
        const url = this.isEditing 
          ? `http://127.0.0.1:5000/products/${this.productId}` 
          : 'http://127.0.0.1:5000/products';
  
        await fetch(url, {
          method: method,
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.product)
        });
        
        this.$emit('product-saved'); // Emitir evento al componente padre para actualizar la lista
        this.resetForm();
      },
      resetForm() {
        this.product.name = '';
        this.product.price = null;
        this.isEditing = false;
        this.productId = null;
      },
      cancelEdit() {
        this.resetForm();
      },
      setProduct(product) {
        this.product = { ...product };
        this.productId = product.id;
        this.isEditing = true;
      }
    }
  };
  </script>
  
  <style scoped>
  .form-group {
    margin-top: 20px;
  }
  </style>
  