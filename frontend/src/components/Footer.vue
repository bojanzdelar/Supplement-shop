<template>
  <footer class="bg-dark text-muted mt-5">
    <div class="container py-5">
      <div class="row">
        <div class="col-md-6 col-lg-3 mx-auto mb-4">
          <router-link to="/" class="navbar-brand">
            <img
              src="../assets/images/logo/MPLogo.svg"
              width="130"
              height="70"
              class="d-inline-block align-text-top mb-3"
            />
          </router-link>
          <h6 class="fw-bold mb-3">Follow Us</h6>
          <div>
            <a
              href="http://www.facebook.com/musclepharm"
              class="text-reset pe-2"
            >
              <i class="bi bi-facebook"></i>
            </a>
            <a
              href="http://www.twitter.com/musclepharm"
              class="text-reset px-2"
            >
              <i class="bi bi-twitter"></i>
            </a>
            <a
              href="http://www.instagram.com/musclepharm"
              class="text-reset px-2"
            >
              <i class="bi bi-instagram"></i>
            </a>
            <a
              href="http://www.youtube.com/musclepharm"
              class="text-reset px-2"
            >
              <i class="bi bi-youtube"></i>
            </a>
          </div>
        </div>

        <div class="col-md-6 col-lg-3 mx-auto mb-4">
          <h6 class="text-uppercase fw-bold mb-4">Help</h6>
          <div>
            <router-link
              to="/privacy-policy"
              class="text-reset text-decoration-none"
            >
              Privacy policy
            </router-link>
          </div>
          <div>
            <router-link
              to="/refund-policy"
              class="text-reset text-decoration-none"
            >
              Refund policy
            </router-link>
          </div>
          <div>
            <router-link to="/contact" class="text-reset text-decoration-none">
              Contact
            </router-link>
          </div>
          <div>
            <router-link to="/account" class="text-reset text-decoration-none">
              Account
            </router-link>
          </div>
          <div>
            <router-link
              to="/international-distributors"
              class="text-reset text-decoration-none"
            >
              Distributors
            </router-link>
          </div>
        </div>

        <div class="col-md-6 col-lg-3 mx-auto mb-4">
          <h6 class="text-uppercase fw-bold mb-4">Company</h6>
          <div>
            <router-link to="/faq" class="text-reset text-decoration-none">
              FAQ
            </router-link>
          </div>
          <div>
            <a
              href="http://www.mpnatural.com"
              class="text-reset text-decoration-none"
            >
              MP Natural
            </a>
          </div>
          <div>
            <a
              href="http://www.fitmiss.com"
              class="text-reset text-decoration-none"
            >
              Fitmiss
            </a>
          </div>
          <div>
            <a
              href="http://www.musclepharm.com"
              class="text-reset text-decoration-none"
            >
              MusclePharm
            </a>
          </div>
          <div>
            <a
              href="http://www.mpnatural.com"
              class="text-reset text-decoration-none"
            >
              Corporate
            </a>
          </div>
        </div>

        <div class="col-md-6 col-lg-3 mx-auto mb-4">
          <h6 class="text-uppercase fw-bold mb-4">Contact us</h6>
          <div>
            <i class="bi bi-geo-alt"></i>4500 Park Granada, Suite 202,
            Calabasas, CA 91302, USA
          </div>
          <div>
            <i class="bi bi-telephone"></i>
            <a
              href="tel:1-800-292-3909"
              class="text-reset text-decoration-none"
            >
              1-800-292-3909
            </a>
          </div>
          <div>
            <i class="bi bi-envelope"></i>
            <a
              href="mailto:customer.service@musclepharm.com"
              class="text-reset text-decoration-none"
            >
              customer.service@musclepharm.com
            </a>
          </div>
        </div>
      </div>
    </div>
    <div class="text-center pb-4">© 2020 MusclePharm. All Rights Reserved.</div>
  </footer>
</template>
