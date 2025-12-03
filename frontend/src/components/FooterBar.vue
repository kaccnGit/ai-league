<template>
  <footer class="footer">
    <div>
      <p>© {{ new Date().getFullYear() }} AI League</p>
      <p class="sub">致力于打造程序员的万能工具台</p>
    </div>
    <div class="links">
      <a href="https://github.com" target="_blank" rel="noreferrer">GitHub</a>
      <a href="mailto:hello@aileague.dev">Contact</a>
    </div>
  </footer>
</template>

<style scoped>
.footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2rem 1.5rem 3rem;
  color: rgba(30, 30, 47, 0.75);
  border-top: 1px solid rgba(106, 90, 224, 0.08);
  flex-wrap: wrap;
  gap: 1rem;
}
.sub {
  margin: 0.2rem 0 0;
  font-size: 0.85rem;
}
.links {
  display: flex;
  gap: 1rem;
}
.links a {
  color: var(--accent-color);
  font-weight: 500;
}
</style>
