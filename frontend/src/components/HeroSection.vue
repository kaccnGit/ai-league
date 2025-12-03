<template>
  <section class="hero card">
    <div>
      <p class="badge">大而全 · 程序员工具宇宙</p>
      <h1>一个站点，搞定工具、AI、灵感</h1>
      <p class="sub">精选几十款在线工具 + 各大模型入门指南，随时扩展</p>
      <div class="cta">
        <el-button type="primary" size="large" @click="$router.push('/tools')">
          直达工具集
        </el-button>
        <el-button size="large" plain @click="$router.push('/ai')">
          浏览 AI 资源
        </el-button>
      </div>
    </div>
    <div class="stats">
      <div>
        <p class="number">40+</p>
        <p>精选工具</p>
      </div>
      <div>
        <p class="number">15+</p>
        <p>AI 平台</p>
      </div>
      <div>
        <p class="number">100%</p>
        <p>H5 体验</p>
      </div>
    </div>
  </section>
</template>

<style scoped>
.hero {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.95), rgba(240, 245, 255, 0.95));
  border: 1px solid rgba(106, 90, 224, 0.12);
}
.badge {
  display: inline-flex;
  padding: 0.35rem 0.75rem;
  border-radius: 999px;
  background: rgba(106, 90, 224, 0.15);
  font-size: 0.85rem;
}
.sub {
  color: rgba(30, 30, 47, 0.7);
}
.cta {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}
.stats {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
  gap: 1rem;
  text-align: center;
}
.number {
  font-size: 2rem;
  margin: 0;
  color: var(--accent-color);
}
</style>
