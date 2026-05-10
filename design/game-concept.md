# Game Concept: 绿盾卫士 (Green Shield Guardian)

*Created: 2026-05-07*
*Status: Draft*

---

## Elevator Pitch

> 这是一款环保主题的塔防RPG游戏，玩家守护神圣纯净核心，指挥植树精灵种植树木净化土地，同时手持利剑击杀来自邪恶工厂的污染怪物，最终率众工人摧毁工厂，拯救地球于全球变暖的危机之中。

---

## Core Identity

| Aspect | Detail |
| ---- | ---- |
| **Genre** | 塔防 + 动作RPG |
| **Platform** | Web（HTML5 Canvas），PC浏览器 |
| **Target Audience** | 8-35岁，关注环保议题的休闲玩家 |
| **Player Count** | 单人 |
| **Session Length** | 单局约15-30分钟 |
| **Monetization** | 免费 |
| **Estimated Scope** | 小型（1-2个月） |
| **Comparable Titles** | 植物大战僵尸、Kingdom Rush、Bloons TD |

---

## Core Fantasy

玩家扮演地球最后的绿色守卫者。一边调度生命精灵建立自然防线，一边亲自上阵挥剑斩杀工业污染怪物。随着装备升级、树林茁壮，感受到人类与自然协力对抗工业破坏的力量，最终率众拆除工厂，让大地重焕绿色生机。

---

## Unique Hook

它像《植物大战僵尸》，**而且**玩家可以亲自持剑参战并选择武器，同时自动化的生态系统（纯净核心→精灵→树木→净化循环）会在后台自运转，让玩家体验人与自然合力抗争的双重满足感。

---

## Player Experience Analysis (MDA Framework)

### Target Aesthetics (What the player FEELS)

| Aesthetic | Priority | How We Deliver It |
| ---- | ---- | ---- |
| **Sensation** (sensory pleasure) | 1 | 卡通粒子特效：精灵撒粉、剑光闪烁、怪物消散烟雾 |
| **Challenge** (obstacle course, mastery) | 2 | 5波难度递增，Boss机制，武器选择策略 |
| **Fantasy** (make-believe) | 3 | 守护者身份认同、环保英雄叙事 |
| **Narrative** (drama, story arc) | 4 | 工厂→5波战斗→拆厂胜利的完整弧线 |
| **Discovery** (exploration) | 5 | 新武器、树木升级带来的新能力体验 |
| **Submission** (relaxation) | 6 | 精灵自动植树的治愈感 |
| **Expression** | N/A | 无 |
| **Fellowship** | N/A | 单人游戏 |

### Key Dynamics (Emergent player behaviors)
- 玩家会主动优先清除喷毒气的骷髅远程怪，保护树木
- 玩家会权衡是先买武器升级还是先升树木
- 玩家会在Boss出现前预判并提前储备金币

### Core Mechanics (Systems we build)

1. **生态循环系统**：纯净核心 → 生成精灵 → 精灵植树 → 树木吸收CO₂/回血 → 维持核心健康
2. **波次入侵系统**：5波怪物从右侧工厂出发，向左攻击，难度递增
3. **战斗武器系统**：玩家手动攻击，金币购买火焰剑/寒冰剑/冰火法杖，Boss前赠灭世之剑
4. **毒气扩散系统**：工厂持续排放污染，树木吸收部分，剩余降低树木生长速度和视觉清晰度
5. **金币经济系统**：击杀怪物获得金币，用于购买武器和树木升级

---

## Player Motivation Profile

### Primary Psychological Needs Served

| Need | How This Game Satisfies It | Strength |
| ---- | ---- | ---- |
| **Competence** | 武器选择、怪物击杀的打击感、五波全清成就感 | Core |
| **Autonomy** | 武器购买顺序自由选择、攻击目标自主决定 | Supporting |
| **Relatedness** | 环保主题引发现实共鸣，胜利结局有意义 | Supporting |

### Player Type Appeal (Bartle Taxonomy)

- [x] **Achievers** — 击杀计数、金币积累、五波全清成就
- [ ] **Explorers** — 无隐藏内容
- [ ] **Socializers** — 单人游戏
- [x] **Competitors** — 高分挑战（可选扩展：最短时间清关）

### Flow State Design

- **Onboarding curve**：前30秒展示精灵自动植树，引导玩家点击攻击第一只怪物，UI高亮商店按钮
- **Difficulty scaling**：第1-2波：普通扭头怪；第3波：加入山羊怪；第4波：加入骷髅+mini-Boss；第5波：大Boss
- **Feedback clarity**：击中特效+金币飞出动画，树木健康度颜色反馈，纯净核心光晕强弱
- **Recovery from failure**：核心被摧毁→游戏结束画面显示环保提示语，可立即重玩

---

## Core Loop

### Moment-to-Moment (30 seconds)
点击/挥剑攻击怪物 → 获得金币 → 观察战场 → 决策：继续攻击还是打开商店购买

### Short-Term (5-15 minutes)
一波怪物入侵 → 清除怪物 → 波间休息（精灵植树，回血，考虑升级）→ 下一波

### Session-Level (15-30 minutes)
完整5波战斗 → 最终Boss → 胜利过场动画（工人拆厂、绿色恢复大地） → 环保结语

### Long-Term Progression
单局游戏，无跨局存档。复玩价值来自：尝试不同武器购买顺序、追求更高分数、快速通关挑战

### Retention Hooks
- **Curiosity**：第一次见到大Boss的视觉冲击
- **Investment**：接近通关时不想放弃
- **Mastery**：熟悉怪物出现规律后优化策略

---

## Game Pillars

### Pillar 1: 自然与人的协力
游戏中玩家主动战斗（武器）和被动生态（精灵/树木）缺一不可，两套系统必须同等重要。

*Design test*: 若某设计让纯持剑即可无视生态系统通关，违反此柱。

### Pillar 2: 卡通趣味感
所有视觉元素（怪物、特效、UI）必须保持欢快卡通风格，不走暗黑路线，让不同年龄段都能接受。

*Design test*: 若怪物设计让8岁儿童感到恐惧，需重新设计。

### Pillar 3: 环保寓意清晰
游戏结局和过程中的每一个机制都要能对应现实中的环保行动，让玩家产生共鸣。

*Design test*: 若有玩家在通关后不知道游戏在讲环境保护，需加强叙事提示。

### Anti-Pillars

- **NOT 复杂策略游戏**：不做多路线塔防，不做复杂建造，保持操作简单易上手
- **NOT 黑暗末日风**：不用写实画风，不强调污染的残酷，保持积极乐观基调
- **NOT 无尽模式**：游戏有明确结局，有环保意义的收尾，不做无限刷波次

---

## Inspiration and References

| Reference | What We Take From It | What We Do Differently | Why It Matters |
| ---- | ---- | ---- | ---- |
| 植物大战僵尸 | 波次系统、从右到左的入侵逻辑、卡通怪物设计 | 玩家可主动参战，有明确环保主题结局 | 验证了该核心模式的趣味性 |
| Kingdom Rush | 波间升级决策、多种敌人类型 | 简化建造，加入RPG装备系统 | 验证了经济升级系统的策略深度 |
| Stardew Valley | 治愈感的自然生长动画 | 加入战斗压力，不做纯放置 | 验证了生态自运转带来的满足感 |

**Non-game inspirations**: 地球日宣传海报的明亮色彩风格；宫崎骏《风之谷》中自然与人类的对抗与和解主题

---

## Target Player Profile

| Attribute | Detail |
| ---- | ---- |
| **Age range** | 8-35岁 |
| **Gaming experience** | 休闲到中度玩家 |
| **Time availability** | 随时可玩，单局15-30分钟 |
| **Platform preference** | PC浏览器，可能扩展到移动端 |
| **Current games they play** | 植物大战僵尸、迷你地铁、小游戏合集 |
| **What they're looking for** | 轻松但有成就感，有意义感的游戏体验 |
| **What would turn them away** | 过于复杂的操作、太难通关、无聊的重复感 |

---

## Technical Considerations

| Consideration | Assessment |
| ---- | ---- |
| **Recommended Engine** | 纯 HTML5 + JavaScript + Canvas 2D（无需安装，浏览器直接运行） |
| **Key Technical Challenges** | 粒子特效系统性能优化；精灵AI寻路；碰撞检测 |
| **Art Style** | 2D卡通，矢量风格，鲜艳色彩 |
| **Art Pipeline Complexity** | 低（代码绘制+简单图形） |
| **Audio Needs** | 适中（背景音乐+打击音效+胜利音乐） |
| **Networking** | 无 |
| **Content Volume** | 5波怪物、3种怪物类型、2个Boss、5种武器、3个树木等级 |
| **Procedural Systems** | 无，固定设计 |

---

## Risks and Open Questions

### Design Risks
- 波间休息时间设计难以平衡（太短压力过大，太长无聊）
- 自动生态系统和玩家主动战斗的贡献比例需要反复测试

### Technical Risks
- Canvas 2D大量粒子特效可能在低端设备上掉帧
- 怪物AI的寻路在树木密布时可能出现卡路问题

### Scope Risks
- 美术全用代码绘制，风格统一性依赖开发者审美

### Open Questions
- 精灵数量上限设为多少合适？（当前设想：根据核心健康度，最多8个精灵）
- 树木对毒气的吸收率公式如何设计才能保证游戏平衡？

---

## MVP Definition

**Core hypothesis**: 玩家在面对波次入侵时，能同时享受主动战斗的爽感和观察生态自运转的满足感。

**Required for MVP**:
1. 生态循环系统（核心→精灵→树木）可运行
2. 至少1波怪物入侵与基础战斗
3. 金币掉落与1种武器购买

**Explicitly NOT in MVP**:
- 完整5波
- 特效动画
- 大Boss

### Scope Tiers

| Tier | Content | Features | Timeline |
| ---- | ---- | ---- | ---- |
| **MVP** | 1波怪物 | 生态循环+基础战斗+金币 | 1周 |
| **Vertical Slice** | 3波+1 mini-Boss | 武器升级+树木升级+毒气系统 | 2-3周 |
| **Alpha** | 5波+大Boss | 完整系统+特效+音效 | 4-6周 |
| **Full Vision** | 完整游戏+胜利过场 | 所有系统+动画+结局 | 6-8周 |

---

## Next Steps

- [x] 游戏概念文档完成
- [ ] 分解核心系统，创建各系统GDD文档
- [ ] 创建技术架构决策文档
- [ ] 原型开发：生态循环系统
- [ ] 原型开发：战斗系统
- [ ] 整合测试
