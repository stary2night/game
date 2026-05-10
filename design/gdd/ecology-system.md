# 生态循环系统 (Ecology Cycle System)

> **Status**: Draft
> **Author**: Game Designer
> **Last Updated**: 2026-05-07
> **Implements Pillar**: 自然与人的协力

## Summary

纯净核心、植树精灵和绿色树木构成一套自运转的生态循环，在玩家主动战斗的同时提供持续的被动防御力和治愈力。核心健康度越高，精灵越多，树木越茂盛，生态系统自我强化。

> **Quick reference** — Layer: `Foundation` · Priority: `MVP` · Key deps: `pollution-system.md, wave-system.md`

---

## Overview

生态循环是游戏的被动防御支柱。纯净核心位于领地中央，定期生成植树精灵；精灵在空地上种植树木；树木吸收毒气并为核心提供微量治愈。三者形成正向循环：核心健康 → 更多精灵 → 更多树木 → 更多治愈。怪物通过攻击树木和核心来破坏此循环。

---

## Player Fantasy

玩家应感受到：我建立了一片生机盎然的绿色领地，小精灵们在我的保护下勤劳地种树，树林越来越茂密，大地越来越有活力。即使我暂时顾不过来，大自然也在自我修复。

---

## Detailed Design

### Core Rules

**纯净核心 (Pure Core)**
1. 核心位于领地最左侧中央，固定不可移动
2. 核心有最大生命值 `CORE_MAX_HP = 500`
3. 核心每秒自动恢复 `CORE_BASE_REGEN = 1` 点生命（被攻击状态下暂停回复）
4. 核心根据当前HP百分比决定精灵生成速率（见公式）
5. 核心HP归零 → 游戏失败
6. 核心发出绿色光晕，光晕强度与HP百分比正相关

**植树精灵 (Tree Planting Sprite)**
1. 精灵由核心生成，初始出现于核心位置
2. 精灵在领地内寻找最近的空白格子，飞行过去种树
3. 精灵种完树后消失（不重复使用）
4. 精灵飞行速度：`SPRITE_SPEED = 80 px/s`
5. 精灵同时存在上限：`MAX_SPRITES = 8`
6. 精灵不能被怪物攻击（精灵代表自然意志，无形无体）
7. 精灵种树时播放撒花粉粒子特效

**绿色树木 (Green Tree)**
1. 树木种植于领地内网格的空白格子上
2. 树木有生命值，初始 `TREE_HP = 80`（可通过金币升级）
3. 树木每秒吸收周围范围内 `TREE_CO2_ABSORB = 3` 单位毒气浓度
4. 树木HP > 0 时，每秒为核心提供 `TREE_HEAL = 0.2` 点治愈
5. 树木HP归零时枯死，格子变为空白（可被精灵重新种植）
6. 树木有3个视觉状态：健康（绿色饱满）/ 受损（黄色变小）/ 濒死（棕色枯萎）

### States and Transitions

**纯净核心状态**

| State | Entry Condition | Exit Condition | Behavior |
|-------|----------------|----------------|----------|
| 活跃 (Active) | 初始状态 | HP ≤ 0 | 正常生成精灵，发出光晕，自动回复HP |
| 受攻击 (Under Attack) | 受到怪物伤害 | 3秒内无伤害 | 停止自动回复，光晕闪烁红色 |
| 毁灭 (Destroyed) | HP ≤ 0 | — | 触发游戏失败流程 |

**树木状态**

| State | Entry Condition | Exit Condition | Behavior |
|-------|----------------|----------------|----------|
| 幼苗 (Seedling) | 刚被种植 | 2秒后 | 不吸收毒气，不治愈核心 |
| 健康 (Healthy) | HP > 50% | HP ≤ 50% | 正常吸收毒气，治愈核心 |
| 受损 (Damaged) | HP 20%-50% | HP < 20% 或回复到 > 50% | 吸收效率×0.5，治愈效率×0.5 |
| 濒死 (Dying) | HP < 20% | HP ≤ 0 或回复到 > 20% | 不吸收毒气，不治愈 |
| 枯死 (Dead) | HP ≤ 0 | 精灵重新种植 | 格子为空白可重种 |

### Interactions with Other Systems

| System | Interaction |
|--------|-------------|
| 毒气扩散系统 | 树木从毒气系统读取当前格子毒气浓度，执行吸收 |
| 波次入侵系统 | 怪物攻击树木和核心，造成HP减少 |
| 金币经济系统 | 升级树木等级时修改 TREE_HP 和 TREE_CO2_ABSORB |
| 武器特效系统 | 玩家武器保护核心和树木，不直接交互，但怪物击杀减少对生态的威胁 |

---

## Formulas

### 精灵生成间隔公式

```
sprite_spawn_interval = BASE_INTERVAL / (core_hp_pct * HEALTH_FACTOR)
```

| Variable | Type | Range | Source | Description |
|----------|------|-------|--------|-------------|
| BASE_INTERVAL | float | 8.0s | 配置 | 核心满血时的精灵生成基础间隔 |
| core_hp_pct | float | 0.01 - 1.0 | 核心当前HP | 核心HP百分比（最低0.01防止除零） |
| HEALTH_FACTOR | float | 1.0-2.0 | 配置 | 健康度对生成速率的放大系数 |

**Expected output range**: 4s（满血）到 80s（2% HP）
**Edge case**: core_hp_pct 低于0.01时钳制为0.01

### 树木总治愈量公式

```
total_heal_per_sec = count_healthy_trees * TREE_HEAL + count_damaged_trees * TREE_HEAL * 0.5
```

**Expected output range**: 0（无树）到 1.6/s（8棵满格满血树）

---

## Edge Cases

| Scenario | Expected Behavior | Rationale |
|----------|------------------|-----------|
| 精灵数量已达上限时核心触发生成 | 跳过本次生成，等待下一个周期 | 防止精灵溢出内存 |
| 领地所有格子都已有树木 | 精灵在核心附近待机，不消失 | 树木全满时精灵无需消耗，等待有树枯死 |
| 核心HP在1时被攻击 | 先扣HP到0，再触发游戏失败，不处理负数HP | 防止状态错误 |
| 树木被种在怪物正在经过的格子 | 树木正常种植，怪物可以攻击它 | 精灵不检查怪物位置 |
| 同一格子两个精灵同时到达 | 先到者种树，后到者寻找下一个空格 | 先到先得原则 |

---

## Dependencies

| System | Direction | Nature of Dependency |
|--------|-----------|---------------------|
| 毒气扩散系统 | 本系统依赖 | 读取毒气浓度进行吸收计算 |
| 金币经济系统 | 金币系统依赖本系统 | 购买树木升级时修改本系统参数 |
| 波次入侵系统 | 波次系统依赖本系统 | 怪物攻击目标来自本系统实体 |
| 游戏结束系统 | 游戏结束系统依赖本系统 | 监听核心HP归零事件 |

---

## Tuning Knobs

| Parameter | Current Value | Safe Range | Effect of Increase | Effect of Decrease |
|-----------|--------------|------------|-------------------|-------------------|
| CORE_MAX_HP | 500 | 300-800 | 游戏更宽容，压力减小 | 游戏更紧张，错误代价更高 |
| CORE_BASE_REGEN | 1/s | 0-3/s | 核心更容易维持高血量 | 核心更脆弱 |
| BASE_INTERVAL | 8.0s | 5-15s | 精灵更少，树木更稀疏 | 精灵更多，树木更快覆盖领地 |
| MAX_SPRITES | 8 | 4-12 | 领地填充更快，压力减小 | 精灵资源稀缺，战略性更强 |
| TREE_HP | 80 | 40-150 | 树木更耐打，保护核心能力强 | 树木脆弱，怪物推进更快 |
| TREE_HEAL | 0.2/s | 0.05-0.5/s | 生态治愈贡献增大 | 玩家更依赖武器主动防守 |
| SPRITE_SPEED | 80 px/s | 50-150 px/s | 精灵更快到达目标 | 精灵路途长，响应慢 |

---

## Visual/Audio Requirements

| Event | Visual Feedback | Audio Feedback | Priority |
|-------|----------------|---------------|----------|
| 核心生成精灵 | 绿色光环扩散波纹 | 轻柔魔法音效 | HIGH |
| 精灵飞行中 | 小精灵卡通形象+粒子尾迹 | 轻快飞行音效（循环） | HIGH |
| 精灵种树 | 花粉粒子爆发，幼苗冒出地面动画 | 清脆种植音效 | HIGH |
| 树木受损 | 树叶脱落粒子，颜色从绿→黄 | 树木受击音效 | MEDIUM |
| 树木枯死 | 枯萎动画，树变灰褐色再消失 | 悲伤短音效 | MEDIUM |
| 核心受攻击 | 光晕变红闪烁，血条抖动 | 受伤警报音效 | HIGH |
| 核心HP低于25% | 屏幕边缘红色脉动提示 | 持续警报背景音 | HIGH |

---

## Game Feel

### Feel Reference
应有《星露谷物语》中播种的满足感 + 《植物大战僵尸》中植物被吃掉的紧张感。精灵飞行要轻盈活泼，不能机械；树木生长要有生命力，不能瞬间出现。

### Input Responsiveness

| Action | Max Input-to-Response Latency (ms) | Frame Budget (at 60fps) | Notes |
|--------|-----------------------------------|------------------------|-------|
| 无（生态系统全自动）| — | — | 玩家不直接操作此系统 |

### Impact Moments

| Impact Type | Duration (ms) | Effect Description | Configurable? |
|-------------|--------------|-------------------|---------------|
| 核心濒死警报 | 持续 | 屏幕边缘红色脉动 | Yes |
| 精灵种树 | 600ms | 花粉粒子爆炸 | Yes |
| 树木枯死 | 500ms | 枯萎+消散动画 | Yes |

---

## UI Requirements

| Information | Display Location | Update Frequency | Condition |
|-------------|-----------------|-----------------|-----------|
| 核心HP | 核心实体上方血条 + 左上角数值 | 实时 | 始终显示 |
| 当前精灵数量 | 左侧HUD图标计数 | 实时 | 始终显示 |
| 树木存活数量 | 左侧HUD图标计数 | 实时 | 始终显示 |

---

## Acceptance Criteria

- [ ] 核心每秒生成精灵间隔与HP百分比成反比（满血8s，半血~11s，低血更慢）
- [ ] 精灵能找到最近空格并飞行过去种树，种完后消失
- [ ] 最多同时存在8个精灵，超限时不再生成
- [ ] 树木受到怪物攻击后HP减少，视觉状态按阈值切换
- [ ] 树木枯死后格子变空白，精灵可重新种植
- [ ] 核心HP归零时触发游戏失败
- [ ] Performance: 生态系统每帧更新在 2ms 内完成

---

## Open Questions

| Question | Owner | Deadline | Resolution |
|----------|-------|----------|-----------|
| 精灵寻路算法：BFS最近空格还是随机空格？ | 开发者 | 原型阶段 | 待测试哪种更有趣 |
| 树木是否应有攻击能力（如荆棘）？ | 设计者 | Vertical Slice | 初期不加，保持生态为纯防御 |
