<template>
  <div class="container mt-5">
    <h1>We Would Like to Hear From You</h1>
    <p>Customer Service Contact Form</p>
    <form @submit.prevent="sendMail">
      <div class="mb-3">
        <label for="firstName" class="form-label">First name</label>
        <input
          v-model="mail.first_name"
          type="text"
          class="form-control"
          id="firstName"
          required
        />
      </div>
      <div class="mb-3">
        <label for="lastName" class="form-label">Last name</label>
        <input
          v-model="mail.last_name"
          type="text"
          class="form-control"
          id="lastName"
          required
        />
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input
          v-model="mail.email"
          type="email"
          class="form-control"
          id="email"
          required
        />
      </div>
      <div class="mb-3">
        <label for="subject" class="form-label">Subject</label>
        <input
          v-model="mail.subject"
          type="text"
          class="form-control"
          id="subject"
          required
        />
      </div>
      <div class="mb-3">
        <label for="message" class="form-label">Message</label>
        <textarea
          v-model="mail.message"
          class="form-control"
          id="message"
          rows="3"
          required
        ></textarea>
      </div>
      <div class="mb-3">
        <input type="submit" class="btn btn-success" value="Submit" />
      </div>
    </form>
  </div>
</template>

<script>
import axios from "@/service/index.js";

export default {
  name: "Contact",
  data() {
    return {
      mail: {},
    };
  },
  methods: {
    async sendMail() {
      await axios
        .post("/mail", this.mail)
        .then(() => {
          window.alert("Mail sent!");
          this.mail = {};
        })
        .catch(() => {
          window.alert("Something went wrong! Please try again later.");
        });
    },
  },
};
</script>
