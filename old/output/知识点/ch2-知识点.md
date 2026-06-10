# 第 2 章 牛顿运动定律

## 一、知识点总结

### 2.1 牛顿运动三定律
- **牛顿第一定律**：任何质点都保持静止或匀速直线运动状态，直到其它物体作用的力迫使它改变这种状态为止。
  - 引进了两个重要概念：① 惯性（用质量量度）；② 力（使质点改变运动状态的原因）。
  - 当 $\sum \vec{F}_i = 0$ 时，质点处于静止或匀速直线运动状态（静力学基本方程）。
- **牛顿第二定律**：某时刻质点动量对时间的变化率正比于该时刻作用在质点上所有力的合力。
  - 一般形式：$\sum \vec{F}_i = \dfrac{\mathrm{d}(m\vec{v})}{\mathrm{d}t} = \dfrac{\mathrm{d}m}{\mathrm{d}t}\vec{v} + m\dfrac{\mathrm{d}\vec{v}}{\mathrm{d}t}$。
  - 当质量不随时间变化时：$\sum \vec{F}_i = m\dfrac{\mathrm{d}\vec{v}}{\mathrm{d}t} = m\vec{a}$。
  - 直角坐标系下：$\sum F_{ix} = m\dfrac{\mathrm{d}^2 x}{\mathrm{d}t^2},\; \sum F_{iy} = m\dfrac{\mathrm{d}^2 y}{\mathrm{d}t^2},\; \sum F_{iz} = m\dfrac{\mathrm{d}^2 z}{\mathrm{d}t^2}$。
  - 自然坐标下：$\sum F_n = ma_n = \dfrac{mv^2}{\rho} = \dfrac{m}{\rho}\!\left(\dfrac{\mathrm{d}s}{\mathrm{d}t}\right)^{\!2}$，$\sum F_\tau = ma_\tau = m\dfrac{\mathrm{d}v}{\mathrm{d}t} = m\dfrac{\mathrm{d}^2 s}{\mathrm{d}t^2}$。
  - 讨论：① 第二定律只适用于质点；② 质量不能当常量的两种情况——质量增减（火箭、雨滴）、高速运动（$v>10^6$ m/s）相对论效应。
- **牛顿第三定律**：$\vec{F} = -\vec{F}'$（成对性、同时性）。适用于接触力，对非接触力因有限传播速度存在延迟效应。

### 2.2 力学中常见的几种力
- **万有引力**：$F = G\dfrac{m_1 m_2}{r^2}$，$G = 6.67\times10^{-11}\,\mathrm{m^3\cdot kg^{-1}\cdot s^{-2}}$，矢量 $\vec{F}_{21} = -G\dfrac{m_1 m_2}{r^2}\vec{r}^0$。
  - 引力质量 = 惯性质量（实验表明对同一物体总相等）。
  - 球对称物体/均匀球体与外部质点的作用可直接用万有引力公式。
  - 球内 $x<R$ 处 $F = G\dfrac{Mm x}{R^3}$（由 $M' = \rho\,\dfrac{4}{3}\pi x^3$）。
  - **重力**：考虑地球自转后 $P = G\dfrac{Mm}{R^2}(1 - 0.0035\cos^2\varphi)$，$\varphi$ 为地理纬度角。
- **弹性力**：物体接触且发生微小形变时产生；弹簧的弹性力 $f = -kx$（胡克定律）；绳内部产生弹性张力。
- **摩擦力**：
  - 静摩擦力（$0 \le f_s \le \mu_0 N$，$\mu_0$ 为最大静摩擦系数，$f_{\max} = \mu_0 N$）。
  - 滑动摩擦力 $f = \mu N$（$\mu$ 为滑动摩擦系数）。

### 2.3 牛顿运动定律的应用
- 三类典型问题：① 已知运动求力；② 已知力求运动；③ 已知运动与力的某些方面求未知方面。
- 求解关键：力 → 加速度 → 运动。加速度起"桥梁"作用。
- **一般步骤**：① 隔离法取研究对象；② 画受力分析图，分析力随什么参量变化；③ 选坐标系；④ 由牛顿第二定律写运动微分方程与辅助方程，进行微分变量替换并积分；⑤ 讨论结果的物理意义。
- **变力问题处理**（重点）：
  - 力随时间 $F=f(t)$：直接积分，$m\dfrac{\mathrm{d}v_x}{\mathrm{d}t} = f(t) \Rightarrow v_x = v(t)+c$；$x = \int v_x \mathrm{d}t = x(t) + c_2$。
  - 力随速度 $F=f(v)$：$\mathrm{d}t = m\dfrac{\mathrm{d}v}{f(v)} \Rightarrow t - t_0 = m\displaystyle\int \dfrac{\mathrm{d}v}{f(v)}$。
  - 力随位移 $F=f(x)$：$f(x) = m v \dfrac{\mathrm{d}v}{\mathrm{d}x} \Rightarrow \int f(x)\mathrm{d}x = \dfrac{1}{2}m(v^2 - v_0^2)$。

### 2.4 牛顿运动定律的适用范围
- **惯性系**：牛顿运动定律适用的参照系。地面参考系近似惯性系；相对于惯性系作匀速直线运动的参照系都是惯性系。
- **惯性力**：在非惯性系中，引入虚拟力 $\vec{F}_0 = -m\vec{a}_e$，使 $\vec{F} + \vec{F}_0 = m\vec{a}_r$ 形式上成立。
  - 惯性力无施力者、无反作用力，不满足牛顿第三定律。
  - 概念可推广到非平动的非惯性系。
- **适用范围**：宏观物体的低速运动。高速 → 相对论；微观 → 量子力学。

## 二、公式汇总

- 公式1：$\sum \vec{F}_i = \dfrac{\mathrm{d}(m\vec{v})}{\mathrm{d}t}$
  说明：牛顿第二定律最一般形式，适用于质量变化情形；$\vec{p} = m\vec{v}$ 为动量。

- 公式2：$\sum \vec{F}_i = m\dfrac{\mathrm{d}\vec{v}}{\mathrm{d}t} = m\vec{a}$
  说明：质量不变时牛顿第二定律的常见形式，仅适用于质点。

- 公式3：$\sum F_{ix} = m\dfrac{\mathrm{d}^2 x}{\mathrm{d}t^2},\; \sum F_{iy} = m\dfrac{\mathrm{d}^2 y}{\mathrm{d}t^2},\; \sum F_{iz} = m\dfrac{\mathrm{d}^2 z}{\mathrm{d}t^2}$
  说明：直角坐标分量式，可用于求解质点运动的轨迹。

- 公式4：$\vec{F} = -\vec{F}'$
  说明：牛顿第三定律，作用力与反作用力大小相等、方向相反、同一直线、同生同灭。

- 公式5：$F = G\dfrac{m_1 m_2}{r^2}$
  说明：万有引力定律大小表达式，$G = 6.67\times10^{-11}\,\mathrm{m^3 kg^{-1} s^{-2}}$，适用于两质点间相互作用。

- 公式6：$\vec{F}_{21} = -G\dfrac{m_1 m_2}{r^2}\vec{r}^0$
  说明：万有引力矢量表达式，$\vec{r}^0$ 由 $m_1$ 指向 $m_2$ 的单位矢量；负号表示 $m_2$ 受力方向指向 $m_1$。

- 公式7：$P = G\dfrac{Mm}{R^2}(1 - 0.0035\cos^2\varphi)$
  说明：考虑地球自转后物体重力大小，$\varphi$ 为地理纬度角，$R$ 为地球半径，$M$ 为地球质量。

- 公式8：$f = -kx$
  说明：胡克定律，弹簧形变量 $x$（形变方向），$k$ 为劲度系数，负号表示力方向与形变方向相反。

- 公式9：$f_{\max} = \mu_0 N$，$f = \mu N$
  说明：最大静摩擦力与滑动摩擦力公式，$\mu_0$、$\mu$ 分别为最大静摩擦系数和滑动摩擦系数，$N$ 为正压力。

- 公式10：$\sum F_n = m\dfrac{v^2}{\rho}$，$\sum F_\tau = m\dfrac{\mathrm{d}v}{\mathrm{d}t}$
  说明：牛顿第二定律在自然坐标下的分量形式，法向提供向心力，切向改变速度大小。

- 公式11：$m\dfrac{\mathrm{d}v_x}{\mathrm{d}t} = f(t) \;\Rightarrow\; v_x = \int \dfrac{1}{m}f(t)\mathrm{d}t + c$
  说明：力随时间变化问题，直接对 $t$ 积分，$c$ 由初条件确定。

- 公式12：$t - t_0 = m\displaystyle\int \dfrac{\mathrm{d}v}{f(v)}$
  说明：力随速度变化问题，作变量分离后积分。

- 公式13：$\int f(x)\mathrm{d}x = \dfrac{1}{2}m(v^2 - v_0^2)$
  说明：力随位移变化问题，使用链式法则 $a = v\,\mathrm{d}v/\mathrm{d}x$。

- 公式14：$\vec{F}_0 = -m\vec{a}_e$
  说明：非惯性系中的惯性力（虚拟力），$\vec{a}_e$ 为非惯性系相对惯性系的牵连加速度。

- 公式15：$\vec{F} + \vec{F}_0 = m\vec{a}_r$
  说明：非惯性系中牛顿第二定律的形式上成立表达式，$\vec{a}_r$ 为相对非惯性系的加速度。
