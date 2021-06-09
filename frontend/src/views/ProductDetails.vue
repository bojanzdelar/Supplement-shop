<template>
    <div class="container">
        <div class="row">
            <div class="col-md-6">
                <img 
                    :src="product.image" 
                    alt="product.name" 
                    class="img-fluid"
                />
            </div>
            <div class="col-md-6">
                <h2>{{ product.name }}</h2>
                <p>{{ product.description}}</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "ProductDetails",
    data() {
        return {
            product: {}
        }
    },
    methods: {
        getProduct() {
            axios.get(`http://localhost:5000/api/product/${this.$route.params['id']}`)
                .then((response) => {
                    this.product = response.data;
                });
        }
    },
    created() {
        this.getProduct();
    }
}
</script>
