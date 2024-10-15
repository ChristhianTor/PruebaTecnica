<template>
  <div id="app">
    <div class="container">
      <h1>Gestión de Productos</h1>
      <ProductForm @product-saved="fetchProducts" />
      <ProductList @edit-product="editProduct" />
    </div>
  </div>
</template>

<script>
import ProductForm from './components/ProductForm.vue';
import ProductList from './components/ProductList.vue';

export default {
  components: {
    ProductForm,
    ProductList
  },
  methods: {
    editProduct(product) {
      this.$refs.productForm.setProduct(product);  // Método para preparar el formulario para edición
    }
  }
};
</script>

<style>
.container {
  margin-top: 20px;
}
</style>
