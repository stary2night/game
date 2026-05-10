# 毒气扩散系统 (Pollution Spread System)

> **Status**: Draft
> **Author**: Game Designer
> **Last Updated**: 2026-05-07
> **Implements Pillar**: 环保寓意清晰

## Summary

工厂持续向领地排放毒气，毒气以扩散方式蔓延，降低树木生长速度和吸收效率。树木可吸收部分毒气，玩家感受到"污染vs自然净化"的动态博弈。毒气浓度也通过视觉污染效果直观呈现全球变暖的威胁。

> **Quick reference** — Layer: `Foundation` · Priority: `MVP` · Key deps: `ecology-system.md, wave-system.md`

---

## Overview

工厂位于领地右侧边缘，持续产生污染浓度值。毒气按格子扩散，从右向左蔓延，每格有当前毒气浓度值。树木通过吸收减少周围格子浓度。骷髅怪物攻击也会增加局部毒气浓度。高毒气浓度会降低精灵植树效率，形成"污染恶化→生态弱化→更多污染"的负反馈循环，增加游戏紧张感。

---

## Player Fantasy

玩家应感受到：工厂冒出的黑烟在慢慢侵蚀我的领地，树木是我抵抗污染的第一道防线。当树木密集时空气变清澈，当树木减少时领地变得灰蒙蒙的，这种视觉变化让环保主题感同身受。

---

## Detailed Design

### Core Rules

1. 领地被划分为网格，每格有 `pollution_level`（0.0-1.0）
2. 工厂每秒向最右侧一列格子增加 `FACTORY_EMISSION = 0.05` 污染值
3. 每秒，每格向左侧相邻格子扩散 `DIFFUSION_RATE = 0.02` 污染值（同时自身减少该值）
4. 树木每秒吸收其所在格子 `TREE_CO2_ABSORB` 污染值（健康树：3/s，受损树：1.5/s）
5. 格子污染值上限为 1.0，下限为 0.0（钳制）
6. 精灵植树速度受目标格子污染值影响（污染越高，种树动画越慢）
7. 高污染（>0.6）区域内的树木生长速度降低50%
8. 骷髅怪物攻击时，在攻击点周围50px范围内增加 `SKELETON_EMISSION = 0.15` 污染值

### 视觉污染层级

| 污染浓度 | 视觉表现 | 生态影响 |
|----------|----------|----------|
| 0.0 - 0.2 | 背景清澈，蓝天白云 | 无负面影响 |
| 0.2 - 0.4 | 轻微灰色薄雾 | 精灵种树速度-10% |
| 0.4 - 0.6 | 中度黄绿色雾霾 | 精灵种树速度-25%，树木生长速度-25% |
| 0.6 - 0.8 | 浓重橙色污染云 | 精灵种树速度-50%，树木生长速度-50% |
| 0.8 - 1.0 | 深色毒气，能见度低 | 精灵无法进入高污染区域种树 |

### States and Transitions

污染系统无状态机，为连续浓度值模拟。

### Interactions with Other Systems

| System | Interaction |
|--------|-------------|
| 生态循环系统 | 树木从本系统读取格子污染值并执行吸收 |
| 波次入侵系统 | 骷髅攻击触发局部污染增加 |
| 视觉渲染系统 | 读取污染值网格，叠加对应视觉滤镜 |

---

## Formulas

### 污染扩散公式

```
new_pollution[x][y] = pollution[x][y] - DIFFUSION_RATE + incoming_from_right
incoming_from_right = DIFFUSION_RATE * pollution[x+1][y]
```

**每帧更新**：同时计算所有格子，避免顺序依赖。

### 精灵种树速度修正

```
actual_plant_time = BASE_PLANT_TIME * (1 + pollution_level * POLLUTION_SLOWDOWN_FACTOR)
```

| Variable | Type | Range | Source | Description |
|----------|------|-------|--------|-------------|
| BASE_PLANT_TIME | float | 2.0s | 配置 | 无污染时的种树时间 |
| POLLUTION_SLOWDOWN_FACTOR | float | 2.0 | 配置 | 满污染时种树时间变为3倍 |

---

## Edge Cases

| Scenario | Expected Behavior | Rationale |
|----------|------------------|-----------|
| 所有树木死亡时污染扩散速率 | 无树木吸收，污染快速填满整个领地 | 真实模拟无植被的后果 |
| 大Boss阶段3全场污染 | 全局污染值+0.2，超过正常上限可到1.0 | Boss阶段的特殊规则 |
| 玩家购买神圣生命树后 | 吸收值翻倍，高污染区域开始被净化 | 生态投资的正反馈 |

---

## Dependencies

| System | Direction | Nature of Dependency |
|--------|-----------|---------------------|
| 生态循环系统 | 本系统依赖生态系统 | 树木吸收调用本系统减少污染值 |
| 波次入侵系统 | 本系统依赖波次系统 | 骷髅攻击增加污染浓度 |

---

## Tuning Knobs

| Parameter | Current Value | Safe Range | Effect of Increase | Effect of Decrease |
|-----------|--------------|------------|-------------------|-------------------|
| FACTORY_EMISSION | 0.05/s | 0.02-0.1/s | 污染积累更快，压力更大 | 污染很慢，影响可忽略 |
| DIFFUSION_RATE | 0.02/s | 0.01-0.05/s | 污染扩散更快，影响更广 | 污染集中在右侧 |
| POLLUTION_SLOWDOWN_FACTOR | 2.0 | 1.0-3.0 | 污染对生态影响更严重 | 污染基本无影响 |
| SKELETON_EMISSION | 0.15 | 0.05-0.3 | 骷髅更危险，优先级更高 | 骷髅的污染威胁减弱 |

---

## Visual/Audio Requirements

| Event | Visual Feedback | Audio Feedback | Priority |
|-------|----------------|---------------|----------|
| 工厂排放 | 右侧黑色烟雾持续上升 | 工厂机械低鸣声（环境音） | HIGH |
| 污染扩散 | 格子颜色渐变，黄绿色雾霾层 | 无（避免噪音污染） | HIGH |
| 领地被净化 | 净化区域颜色从黄绿→蓝绿→清澈 | 轻柔净化音效 | MEDIUM |
| 高污染警告（>0.7平均浓度） | 屏幕边缘橙色雾化效果 | 低沉持续警告音 | HIGH |

---

## Acceptance Criteria

- [ ] 工厂每秒向右侧格子增加0.05污染值
- [ ] 污染以扩散方式向左蔓延
- [ ] 树木吸收正确减少所在格子污染值
- [ ] 高污染区域精灵种树速度降低
- [ ] 视觉上能看出污染浓度差异（颜色变化）
- [ ] 骷髅攻击后局部污染值增加

---

## Open Questions

| Question | Owner | Deadline | Resolution |
|----------|-------|----------|-----------|
| 是否需要显示污染浓度数值给玩家？ | 设计者 | 原型阶段 | 倾向于只显示视觉变化，不显示数值 |
