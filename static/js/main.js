document.addEventListener("DOMContentLoaded", function() {
    console.log("Nebula AI 终端已启动...");

    // ==========================================
    // 特效 1：丝滑滚动浮现 (Scroll Reveal)
    // ==========================================
    // 选中我们要添加动画的元素：所有特征卡片、巨幕标题、按钮等
    const revealElements = document.querySelectorAll('.feature-card, .hero-title, .hero-subtitle, .badge, .btn-custom, .btn-outline-custom');

    // 初始时给它们加上准备浮现的 CSS class，并错开延迟时间
    revealElements.forEach((el, index) => {
        el.classList.add('reveal-up');
        // 同一排的元素错开 0.15 秒，形成“阶梯式”次第浮现的视觉错觉
        el.style.transitionDelay = `${(index % 3) * 0.15}s`;
    });

    // 监听滚动事件，当元素进入视口时触发动画
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active'); // 加上 active 类，CSS 动画开始执行
                observer.unobserve(entry.target);     // 动画只播放一次，播放完就取消监听，节省性能
            }
        });
    }, {
        threshold: 0.1 // 元素露出 10% 的时候就开始播放动画
    });

    revealElements.forEach(el => observer.observe(el));


    // ==========================================
    // 特效 2：苹果风 3D 卡片悬浮视差交互
    // ==========================================
    const cards = document.querySelectorAll('.feature-card');
    
    cards.forEach(card => {
        // 鼠标在卡片上移动时，实时计算偏转角度
        card.addEventListener('mousemove', e => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left; // 鼠标在卡片内的 X 坐标
            const y = e.clientY - rect.top;  // 鼠标在卡片内的 Y 坐标
            
            // 计算旋转角度 (核心算法：鼠标离中心越远，倾斜角度越大)
            const rotateX = ((y / rect.height) - 0.5) * -12; // 上下倾斜
            const rotateY = ((x / rect.width) - 0.5) * 12;   // 左右倾斜

            // 应用 3D 转换和赛博蓝发光边框
            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
            card.style.borderColor = "rgba(0, 242, 254, 0.5)"; 
            card.style.boxShadow = "0 20px 40px rgba(0, 242, 254, 0.15)";
        });

        // 鼠标移出卡片时，平滑恢复原状
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)';
            card.style.borderColor = "rgba(255, 255, 255, 0.05)";
            card.style.boxShadow = "none";
            
            // 移出时加上过渡动画，让恢复过程更平滑
            card.style.transition = 'transform 0.5s cubic-bezier(0.2, 0.8, 0.2, 1), border-color 0.5s ease';
            setTimeout(() => {
                card.style.transition = 'box-shadow 0.4s ease, border-color 0.4s ease'; // 恢复实时响应
            }, 500);
        });
    });
});