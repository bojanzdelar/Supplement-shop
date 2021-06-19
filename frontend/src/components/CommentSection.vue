<template>
  <div class="row d-flex justify-content-center mt-100 mb-100">
    <div class="col-lg-6">
      <div class="card">
        <div class="card-body text-center">
          <h4 class="card-title">Latest Comments</h4>
        </div>
        <div class="comment-widgets">
          <Comment
            v-for="comment in comments"
            :key="comment.id"
            :username="comment.username"
            :content="comment.content"
            :created="comment.created"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Comment from "@/components/Comment.vue";

export default {
  name: "CommentSection",
  components: {
    Comment,
  },
  data() {
    return {
      comments: [],
    };
  },
  methods: {
    getComments() {
      this.axios.get("/comment").then((response) => {
        this.comments = response.data.filter((comment) => {
          return comment.product_id == this.$route.params["id"];
        });
      });
    },
  },
  created() {
    this.getComments();
  },
};
</script>
