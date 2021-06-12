<template>
  <div class="container">
    <h1>We Would Like to Hear From You</h1>
    <p>Customer Service Contact Form</p>
    <form>
      <div class="mb-3">
        <label for="firstName" class="form-label">First name</label>
        <input type="text" class="form-control" id="firstName" />
      </div>
      <div class="mb-3">
        <label for="lastName" class="form-label">Last name</label>
        <input type="text" class="form-control" id="lastName" />
      </div>
      <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="email" class="form-control" id="email" />
      </div>
      <div class="mb-3">
        <label for="subject" class="form-label">Subject</label>
        <input type="text" class="form-control" id="subject" />
      </div>
      <div class="mb-3">
        <label for="message" class="form-label">Message</label>
        <textarea class="form-control" id="message" rows="3"></textarea>
      </div>
      <div class="mb-3">
        <input type="submit" class="btn btn-success" value="Submit" />
      </div>
    </form>
  </div>
</template>
