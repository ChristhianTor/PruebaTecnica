<template>
    <div class="container">
      <h2>Lista de Productos</h2>
      <table class="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Precio</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in products" :key="product.id">
            <td>{{ product.id }}</td>
            <td>{{ product.name }}</td>
            <td>{{ product.price }}</td>
            <td>
              <button class="btn btn-warning" @click="editProduct(product)">Editar</button>
              <button class="btn btn-danger" @click="deleteProduct(product.id)">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        products: []
      };
    },
    mounted() {
      this.fetchProducts();  // Llama a la función para cargar productos al montar el componente
    },
    methods: {
      async fetchProducts() {
        const response = await fetch('http://127.0.0.1:5000/products');
        this.products = await response.json();  // Guarda los productos en el estado
      },
      async deleteProduct(id) {
        await fetch(`http://127.0.0.1:5000/products/${id}`, {
          method: 'DELETE'
        });
        this.fetchProducts(); // Actualiza la lista después de eliminar
      },
      editProduct(product) {
        this.$emit('edit-product', product);  // Emitir evento al componente padre para indicar que se va a editar
      }
    }
  };
  </script>
  
  <style scoped>
  .table {
    margin-top: 20px;
  }
  </style>
  