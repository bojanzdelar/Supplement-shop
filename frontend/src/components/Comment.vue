<template>
  <div class="d-flex flex-row comment-row m-t-0">
    <div class="p-2">
      <img
        src="https://i.imgur.com/Ur43esv.jpg"
        alt="user"
        width="50"
        class="rounded-circle"
      />
    </div>
    <div class="comment-text w-100">
      <h6 class="font-medium">{{ username }}</h6>
      <span class="m-b-15 d-block">
        {{ content }}
      </span>
      <div class="comment-footer">
        <span class="text-muted float-right">{{ created }}</span>
        <button type="button" class="btn btn-cyan btn-sm">Edit</button>
        <button type="button" class="btn btn-success btn-sm">Publish</button>
        <button type="button" class="btn btn-danger btn-sm">Delete</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Comment",
  props: {
    username: String,
    content: String,
    created: Date,
  },
};
</script>
