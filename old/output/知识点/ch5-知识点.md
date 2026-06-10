# 第 5 章 质点的动量矩与动量矩守恒

## 一、知识点总结

### 5.1 力矩
- **单个质点**：用 $\vec{F}$、$E_k$、$\vec{P}$ 描述动力学性质；但要讨论质点绕某定点的转动，需引入力矩。
- **力矩定义**（对定点 $O$）：$\vec{M}_O = \vec{r}\times\vec{F}$，大小 $|\vec{M}_O| = rF\sin\alpha$（$\alpha$ 为 $\vec{r}$ 与 $\vec{F}$ 夹角）。
  - 方向：由右螺旋法则确定，垂直于 $\vec{r}$ 与 $\vec{F}$ 所成平面；
  - 空间矢量：力矩是空间矢量，不局限于固定平面；
  - 等价表述：$|\vec{M}_O| = $（定点到力作用线的距离）$\times F = $（定点到质点的距离）$\times F_\tau$。
- **质点圆周运动下的力矩**（以圆心 $O$ 为定点）：
  - 切向加速度 $a_\tau = \beta r$（$\beta$ 为角加速度），法向加速度 $a_n = \omega^2 r$；
  - 力矩大小 $M_O = r m a_\tau = r^2 m\beta$。
- **物理意义**：力矩是引起质点绕某一定点转动状态变化（获得角加速度）的原因。

### 5.2 质点的动量矩
- **动量矩（角动量）定义**（对 $O$ 点）：
  \[
    \vec{L}_O = \vec{r}\times\vec{P} = \vec{r}\times m\vec{v},
  \]
  - 大小 $L_O = rp\sin\varphi = mrv\sin\varphi$；
  - 方向由右螺旋法则确定；
  - **特例：圆周运动** $L = rp = mrv$（$\vec{v}\perp\vec{r}$）；
  - 单位：$\mathrm{kg\cdot m^2/s}$。
- **质点对某点的动量矩在过该点的任意轴上的投影**就等于质点对该轴的动量矩。
- **平面运动**：对运动平面内某参考点 $O$ 的动量矩也称为对过 $O$ 垂直于运动平面的轴的动量矩。
- **例**：圆锥摆（$A$ 为摆球圆周轨道圆心，$B$ 为悬挂点，杆与竖直方向夹角 $\alpha$）。
  - 对 $A$ 点：$\vec{L}_A = \vec{r}\times m\vec{v}$，$|\vec{L}_A| = mr^2\omega$，方向沿 $z$ 轴正方向（大小方向均不变）；
  - 对 $B$ 点：$|\vec{L}_B| = mr^2\omega/\sin\alpha$，**方向不断变化**；$\vec{L}_B$ 沿 $z$ 轴投影 $L_{Bz} = L_B\sin\alpha = mr^2\omega$（等于对 $A$ 点的动量矩）。
- **说明**：动量矩只与"垂距"有关——参考点到速度方向直线的垂直距离，不是参考点到质点的距离。
- **质点动量矩定理**（微分形式）：
  \[
    \vec{M} = \frac{\mathrm{d}\vec{L}}{\mathrm{d}t},\quad \vec{M}\mathrm{d}t = \mathrm{d}\vec{L}.
  \]
  - 推导：$\dfrac{\mathrm{d}\vec{L}}{\mathrm{d}t} = \dfrac{\mathrm{d}}{\mathrm{d}t}(\vec{r}\times m\vec{v}) = \vec{r}\times\dfrac{\mathrm{d}(m\vec{v})}{\mathrm{d}t}} + \dfrac{\mathrm{d}\vec{r}}{\mathrm{d}t}\times m\vec{v} = \vec{r}\times\vec{F} + \vec{v}\times m\vec{v} = \vec{M}$。
- **质点动量矩定理**（积分形式）：
  \[
    \int_{t_1}^{t_2}\vec{M}\cdot\mathrm{d}t = \vec{L}_2 - \vec{L}_1.
  \]
  - 物理意义：质点所受合力矩的冲量矩等于质点的动量矩的增量；
  - 冲量矩是动量矩变化的原因，动量矩的变化是力矩对时间的累积结果。
- **质点动量矩守恒定律**：当 $\sum \vec{M}_i = 0$（合外力矩为零）时，$\vec{L} = $ 常矢量。
  - **物理本质**：与空间各向同性（空间旋转对称性）相联系；
  - **适用条件**：系统合外力矩为零；适用于宏观、微观、高速、低速全范围；
  - **特例**：质点只受有心力作用时，质点被限制在与 $\vec{L}$ 垂直的平面内运动，对力心动量矩守恒；
  - **应用**：开普勒第二定律（行星在相等时间内扫过相等面积）由万有引力下的动量矩守恒推出。

### 5.3 质心系的动量矩定律
- **重要结论**：在质心系中不论质心系是惯性系还是非惯性系，动量矩定理仍适用。
  - 原因：质心系中惯性力 $-m_i\vec{a}_C$ 对质心 $C$ 的力矩
    \[
      \vec{M}_{C\text{惯}} = \sum \vec{r}_{Ci}\times(-m_i\vec{a}_C) = -(\sum m_i\vec{r}_{Ci})\times\vec{a}_C = 0.
    \]
  - 因为 $\sum m_i\vec{r}_{Ci} = 0$（$\vec{r}_{Ci}$ 是相对质心的位矢）。
- **质心系动量矩定理**：
  \[
    \vec{M}_C = \frac{\mathrm{d}\vec{L}_C}{\mathrm{d}t}.
  \]
- **体系动量矩分解**：$\vec{L} = \vec{L}_C + \vec{L}_{CM}$
  - 轨道角动量 $\vec{L}_C = \vec{r}_C \times m_C\vec{v}_C$（质心绕定点的动量矩）；
  - 固有角动量 $\vec{L}_{CM} = \sum \vec{r}_{Ci}\times m_i\vec{v}_{Ci}$（各质点相对质心运动的动量矩）。
- **牛顿质点力学的体系**（中心公式 $\vec{F} = \dfrac{\mathrm{d}(m\vec{v})}{\mathrm{d}t}}$ 的三种推广）：
  - 乘 $\mathrm{d}t$ 积分：动量定理；
  - 标积 $\mathrm{d}\vec{s}$ 积分：动能定理；
  - 矢乘 $\vec{r}$：动量矩定理 $\vec{r}\times\vec{F} = \dfrac{\mathrm{d}(\vec{r}\times m\vec{v})}{\mathrm{d}t}}$，$\vec{M} = \dfrac{\mathrm{d}\vec{L}}{\mathrm{d}t}}$。

## 二、公式汇总

- 公式1：$\vec{M}_O = \vec{r}\times\vec{F}$，$|\vec{M}_O| = rF\sin\alpha$
  说明：力对定点 $O$ 的力矩；空间矢量，方向由右螺旋法则确定；$\alpha$ 为 $\vec{r}$ 与 $\vec{F}$ 夹角；既等于力臂乘以 $F$，也等于 $r$ 乘以力的切向分量。

- 公式2：$M_O = rma_\tau = r^2 m\beta$（圆周运动）
  说明：圆周运动下对圆心的力矩大小；$\beta = \mathrm{d}\omega/\mathrm{d}t$ 为角加速度；与转动惯量 $mr^2$ 配合得到 $M = I\beta$。

- 公式3：$\vec{L}_O = \vec{r}\times\vec{P} = \vec{r}\times m\vec{v}$
  说明：质点对 $O$ 点的动量矩（角动量）；方向由右螺旋法则确定；$|\vec{L}_O| = mrv\sin\varphi$；单位 $\mathrm{kg\cdot m^2/s}$；圆周运动 $L = mrv$。

- 公式4：$\vec{M} = \dfrac{\mathrm{d}\vec{L}}{\mathrm{d}t}}$，$\vec{M}\mathrm{d}t = \mathrm{d}\vec{L}$
  说明：质点动量矩定理（微分形式）；合力矩等于质点动量矩对时间的变化率；推导基于 $\vec{r}\times\dfrac{\mathrm{d}(m\vec{v})}{\mathrm{d}t}}$。

- 公式5：$\displaystyle\int_{t_1}^{t_2}\vec{M}\cdot\mathrm{d}t = \vec{L}_2 - \vec{L}_1$
  说明：质点动量矩定理（积分形式）；合力矩的冲量矩等于质点动量矩的增量。

- 公式6：$\sum \vec{M}_i = 0 \Rightarrow \vec{L} = \text{常矢量}$
  说明：质点动量矩守恒定律；合外力矩为零时总动量矩守恒；与空间旋转对称性相联系；是自然界最普适的定律之一。

- 公式7：$\dfrac{\mathrm{d}\vec{S}}{\mathrm{d}t}} = \dfrac{L}{2m}$（面积速度）
  说明：开普勒第二定律的数学表述；面积速度 $\mathrm{d}\vec{S}/\mathrm{d}t$ 是常矢量（有心力场中对力心）。

- 公式8：$\vec{M}_{C\text{惯}} = -\biggl(\sum m_i\vec{r}_{Ci}\biggr)\times\vec{a}_C = 0$
  说明：质心系中惯性力对质心的合力矩为零；因为 $\sum m_i\vec{r}_{Ci} = 0$（相对质心位矢的带权和为零）；这是动量矩定理在质心系中仍成立的根据。

- 公式9：$\vec{M}_C = \dfrac{\mathrm{d}\vec{L}_C}{\mathrm{d}t}}$（质心系动量矩定理）
  说明：不论质心系是惯性系还是非惯性系，质心系中动量矩定理仍成立；与牛顿定律在非惯性系中加惯性力即可使用类比。

- 公式10：$\vec{L} = \vec{L}_C + \vec{L}_{CM}$，其中 $\vec{L}_C = \vec{r}_C\times m_C\vec{v}_C$，$\vec{L}_{CM} = \sum \vec{r}_{Ci}\times m_i\vec{v}_{Ci}$
  说明：体系动量矩分解为轨道角动量（质心绕定点运动）和固有角动量（各质点相对质心运动）之和；如地球的动量矩 = 自转动量矩 + 公转轨道动量矩。
