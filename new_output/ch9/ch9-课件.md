--- PAGE 001 ---
# 一、电磁学核心物理量对照表（TheMapofSymmetry）

我们要对比的是静电场与稳恒磁场（暂不涉及介质中的 D 和 H，先看真空中最基本的关系）：

| 物理特性 | 静电场 (Electrostatics) | 稳恒磁场 (Magnetostatics) | 对应逻辑 |
|:---:|:---:|:---:|:---:|
| 场源 | 电荷 q | 电流 I (运动电荷 qv) | 源的属性 |
| 基本场量 | 电场强度 E | 磁感应强度 B | 描述场的本质 |
| 辅助场量 | 电位移矢量 D | 磁场强度 H | 引入介质后的辅助量 |
| 力学表现 | 电场力 \(F_e = q \vec{E}\) | 磁场力 (洛伦兹力) \(\vec{F}_m = q \vec{v} \times \vec{B}\) | 场对电荷的作用 |
| 基本实验定律 | 库仑定律 | 毕奥-萨伐尔定律 | 场与源的定量关系 |
| 通量定义 | 电通量 \(\Phi_e = \int \vec{E} \cdot d\vec{S}\) | 磁通量 \(\Phi_m = \int \vec{B} \cdot d\vec{S}\) | 穿过曲面的"线"的多少 |
| 高斯定理 (散度) | \(\oint \vec{E} \cdot d\vec{S} = \frac{\sum q}{\varepsilon_0}\) | \(\oint \vec{B} \cdot d\vec{S} = 0\) | 有源场 vs 无源场 |
| 环流定理 (旋度) | \(\oint \vec{E} \cdot d\vec{l} = 0\) | \(\oint \vec{B} \cdot d\vec{l} = \mu_0 \sum I\) | 保守场 vs 非保守场 |
| 能量密度 | \(w_e = \frac{1}{2}\varepsilon_0 E^2\) | \(w_m = \frac{1}{2\mu_0} B^2\) | 能量储存在场中 |

--- PAGE 001 ---
## 9.4 静电场的环路定理 电势能

### 一. 静电力作功的特点

* 单个点电荷产生的电场中

\[A = \int_{a}^{b} \vec{F} \cdot d\vec{l}\]

\[= \int_{a(L)}^{b} q_0 \vec{E} \cdot d\vec{l}\]

\[= \int_{a(L)}^{b} q_0 E \, dl \cos \theta\]

\[= \frac{qq_0}{4\pi\epsilon_0} \int_{r_a}^{r_b} \frac{1}{r^2} dr = \frac{q q_0}{4\pi\epsilon_0} \left( \frac{1}{r_a} - \frac{1}{r_b} \right) \quad \text{（与路径无关）}\]

--- PAGE 001 ---
# 静电场与介质的相互作用

--- PAGE 001 ---
# 一.充满电介质的电容器

电介质：电阻率很大，导电能力很差的物质。分子中的正负电荷束缚的很紧，介质内部几乎没有自由电荷。即绝缘体。

结论：介质充满电场或介质表面为等势面时

\[
\Delta u = \frac{\Delta u_0}{\varepsilon_r} \qquad E = \frac{E_0}{\varepsilon_r}
\]

实验：$+Q \quad -Q$

$\varepsilon_r$ —— 电介质的相对介电常数

$\varepsilon_r \ge 1$ 介质中电场减弱

\[
C = \varepsilon_r C_0
\]

--- PAGE 002 ---
# 大学物理 电磁学

- 电磁学是研究电和磁的相互作用现象，及其规律和应用的物理学分支学科。
- 它是电子技术、电气与控制工程、通信与微波技术、光电技术的主要物理基础。
- 本课程包括静电场、静磁场、变化的电磁和变化的磁场，最后引出麦克斯韦方程组。
- 电磁学强调高等数学中多元函数积分、曲线曲面积分和矢量场论知识的应用。

--- PAGE 002 ---
## 任意带电体系产生的电场中

电荷系 \(q_1\)、\(q_2\)、…的电场中，移动\(q_0\)，有

\[A_{ab} = \int_{a(L)}^{b} \vec{F} \cdot d\vec{l} = \int_{a(L)}^{b} q_0 \vec{E} \cdot d\vec{l}\]

\[= \int_{a(L)}^{b} q_0 \left( \sum_{i=1}^{n} \vec{E}_i \right) \cdot d\vec{l}\]

\[= \sum_{i=1}^{n} \int_{a(L)}^{b} q_0 \vec{E_i} \cdot d\vec{l}\]

\[= \sum_{i} \frac{q_i q_0}{4 \pi \varepsilon_0} \left( \frac{1}{r_{ai}} - \frac{1}{r_{bi}} \right)\]

**结论**

电场力作功只与始末位置有关，与路径无关，所以静电力是保守力，静电场是保守力场。

--- PAGE 002 ---
## 9.7 静电场中的导体

## 一. 导体的静电平衡

**金属导体的电学结构**

金属导体: 带负电的**自由电子**和带正电的晶格点阵组成。当导体不带电也不受外电场的作用时, 只有微观的热运动。自由电子在金属中可以像理想气体分子一样自由运动, 它们为整个金属晶格所共有, 因此称为自由电子气体。

**热平衡特征**: 任意划取的微小体积元内, 自由电子的负电荷和晶体点阵上的正电荷的数目相等, 整个导体或其中任一部分都显现电中性。

--- PAGE 002 ---
## 二. 电介质的极化 极化电荷

<center>无极分子</center>

$p = 0$

无外场时（热运动）

<center>(无极分子电介质)</center>

<center>有极分子</center>

<center>$p = ql$</center>

<center>(有极分子电介质)</center>

--- PAGE 003 ---
# 第9章 静电场

9.1 电荷 库仑定律

9.2 静电场 电场强度

9.3 电通量 高斯定理

9.4 静电场的环路定理 电势能

9.5 电势 电势差

9.6 等势面 *电势与电场强度的微分关系

9.7 静电场中的导体

9.8 电场能量

9.9 静电场中的电介质

--- PAGE 003 ---
## 二. 静电场的环路定理

在静电场中，沿闭合路径移动\(q_0\)，电场力作功

\[A_{ab} = \oint \vec{F} \cdot d\vec{l} = \oint q_0 \vec{E} \cdot d\vec{l}\]

\[= \int_{a(L_1)}^{b} q_0 \vec{E} \cdot d\vec{l} + \int_{b(L_2)}^{a} q_0 \vec{E} \cdot d\vec{l}\]

\[= \int_{a(L_1)}^{b} q_0 \vec{E} \cdot d\vec{l} - \int_{a(L_2)}^{b} q_0 \vec{E} \cdot d\vec{l}\]

\[= 0\]

\[\int_L \vec{E} \cdot d\vec{l} = 0\]

环路定理: 静电场中的电场强度沿闭合曲线的积分为0，即电场强度的**环量为0**。

--- PAGE 003 ---
## · 静电感应

在外电场的作用下，自由电子做宏观定向移动，导体中出现电荷重新分布。静电感应的结果：(1) 导体上的电荷重新分布；(2) 空间电场重新分布。

<center>静电感应现象过程</center>

--- PAGE 003 ---
# 有外场时

- 无极分子电介质

在外电场的作用下，介质表面产生电荷的现象称为电介质的极化。

束缚电荷 $\sigma'$

由于极化，在介质表面产生的电荷称为极化电荷或称束缚电荷。

- 有极分子电介质

$\sigma'$

\[
E = E_0 + E'
\]

束缚电荷 $\sigma'$

--- PAGE 004 ---
## 9.1 电荷 库仑定律

### 一. 电荷

1. 正负性

2. 量子性

\[
Q = ne \quad e = (1.602\,189\,2 \pm 0.000\,004\,6) \times 10^{-19}\,\mathrm{C} \qquad 1\,\mathrm{C} = 1\,\mathrm{A} \cdot \mathrm{s}
\]

3. 守恒性

在一个孤立系统中总电荷量是不变的。即在任何时刻系统中的正电荷与负电荷的代数和保持不变，这称为电荷守恒定律。

4. 相对论不变性

电荷的电量与它的运动状态无关，在一切惯性系中电荷守恒定律都成立，电荷的电量都相同。

--- PAGE 004 ---
\[ \int_L \boldsymbol{E} \cdot \mathrm{d}\boldsymbol{l} = \iint_S (\nabla \times \boldsymbol{E}) \cdot \mathrm{d}\boldsymbol{S} \]

E的旋度

矢量场的斯托克斯定理

\[ \nabla \times \boldsymbol{E} = \boldsymbol{0} \]

静电场是无旋场

\[ \nabla \cdot \boldsymbol{E} = \frac{\rho}{\varepsilon_0} \]

电场的散度——高斯定理

\[ \int_L \boldsymbol{E}^\ast d\boldsymbol{l} = 0 \]

旋度是一个矢量，是环量在空间中的面密度矢量。环量反映场绕一个涡旋中心的空间分布情况，而旋度是空间局部一点上这种旋转程度的描述。

\[ \nabla \times \boldsymbol{F} = \left[ \begin{array}{ccc} i & j & k \\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\ \boldsymbol{F}_x & \boldsymbol{F}_y & \boldsymbol{F}_z \end{array} \right] \]

空间中任意一点的静电场的旋度一定为0，而散度不一定为0。

(1) 环路定理是静电场的另一重要定理，可用环路定理检验一个电场是否不是静电场。这个定理只适用于静电场。

(2) 环路定理要求静电场的电力线不能闭合。

(3) 静电场是有源、无旋场，可引进电势能。

--- PAGE 004 ---
## 1. 静电平衡

导体内部和表面上任何一部分都没有宏观电荷运动，我们就说导体处于静电平衡状态，无论导体是否带电，无论其是否处于外电场中。

## 2. 导体静电平衡的条件

\[
E_{\text{内}} = 0
\]

\[
\vec{E}_{\text{表面}} \perp \text{导体表面}
\]

## 3. 静电平衡导体的电势

导体静电平衡时，导体上各点电势相等，即导体是等势体，表面是等势面。

\[
U_a - U_b = \int_a^b \vec{E} \cdot d\vec{l} = 0
\]

--- PAGE 004 ---
与导体在外电场作用下产生的感应电荷一样，极化电荷也会产生附加电场从而影响空间中总电场的重新分布

$E = E_0 + \tilde{E}'$

内部：削弱场

\[
\tilde{E}_{\text{内}} < \tilde{E}_0
\]

外部：改变场

--- PAGE 005 ---
## 二. 库仑定律

1. **点电荷** 当带电体的大小、形状与带电体间的距离相比可以忽略时，就可把带电体视为一个带电的几何点。（一种理想模型）

2. **库仑定律**

处在静止状态的两个点电荷，在真空中的相互作用力的大小，与每个点电荷的电量成正比，与两个点电荷间距离的平方成反比，作用力的方向沿着两个点电荷的连线。

电荷 \(q_1\) 对 \(q_2\) 的作用力 \(F_{21}\)

\[
F_{21} = k \frac{q_1 q_2}{r^2}
\]

\[
F_{21} = k \frac{q_1 q_2}{r^2} \hat{r}_{21}
\]

*(此处有插图：点电荷相互作用示意图)*

--- PAGE 005 ---
### 三. 电势能

#### 电势能的差

定义：\(q_0\) 在电场中 \(a\)、\(b\) 两点电势能之差等于把 \(q_0\) 自 \(a\) 点移至 \(b\) 点过程中电场力所作的功。

\[A_{ab} = \int_a^b q_0 \overline{E} \cdot d\overline{l} = W_a - W_b\]

--- PAGE 005 ---
## 二. 导体上电荷的分布

由导体的静电平衡条件和静电场的基本性质，可以得出导体上的电荷分布。

### 1. 静电平衡导体的内部处处不带电

证明：在导体内任取体积元 dV

由高斯定理

\[
\int_S \mathbf{E} \cdot d\mathbf{S} = 0, \qquad \sum_i q_i = \int_V \rho \, dV = 0
\]

∴ 体积元任取，导体中各处 $\rho = 0$。

--- PAGE 005 ---
# 导体和电介质放置在电场E中的异同点：

## 一、相似之处（你观察到的"表现形式类似"）

- 两者放入外电场 $E_0$ 后，都会在表面出现电荷：
  - 导体：感应出自由电荷（可流动）。
  - 电介质：极化出束缚电荷（不可流动，只能微小位移）。
- 这些表面电荷都会产生一个反向电场，抵消部分外电场。

所以你的直觉"类似于导体"是对的——从"削弱电场"这个现象上看，两者确实有可类比之处。

## 二、本质不同（必须区分的关键）

| 特性 | 导体 | 电介质 |
|------|------|--------|
| 内部电荷类型 | 自由电子(可宏观移动) | 束缚电荷(只能微观位移) |
| 放入静电场后的最终状态 | 内部总电场 = 0 (静电平衡) | 内部总电场 $\neq$ 0, 只是减弱为 $E_0 / \varepsilon_r$ |
| 削弱程度 | 完全抵消($\varepsilon_r \to \infty$ 的极限) | 部分抵消($\varepsilon_r$ 有限, 通常2~10) |
| 电荷能否移出物体 | 能(接地可转移) | 不能(极化电荷永远束缚在原分子上) |

--- PAGE 006 ---
## 三. 电场力的叠加

\(q_3\) 受的力: \(F = \vec{f}_1 + \vec{f}_2\)
对 n 个点电荷:

\[
\begin{aligned}
F &= \vec{F}_1 + \vec{F}_2 + \cdots + \vec{F}_n \\
&= \sum_i \vec{F}_i = \sum_i \frac{1}{4\pi\varepsilon_0} \frac{q_0 q_i}{r_i^2} \hat{r}_i
\end{aligned}
\]

对电荷连续分布的带电体

\[
d\vec{F} = \frac{q_0 dq}{4\pi\varepsilon_0 r^2} \hat{r}^0
\]

\[
\vec{F} = \int \frac{q_0 dq}{4\pi\varepsilon_0 r^2} \hat{r}^0
\]

*(此处有插图)*

--- PAGE 006 ---
·电势能

\[取势能零点 \quad W_{\cdot0} = 0\]

\(q_0\) 在电场中某点\(a\)的电势能: \(W_a = A_{a\to 0} = \int_{a}^{0} q_0 \vec{E} \cdot d\vec{l}\)

**说明**

(1) 电势能应属于 \(q_0\) 和产生电场的源电荷系统共有。

(2) 电荷在某点电势能的值与零点选取有关,而两点的差值与零点选取无关

(3) 选势能零点原则:

• 当(源)电荷分布在有限范围内时,力势能零点一般选在无穷远处。

• 无限大带电体,势能零点一般选在有限远处一点。

• 实际应用中取大地、仪器外壳等为势能零点。

--- PAGE 006 ---
### 2. 静电平衡导体表面附近的电场强度与导体表面电荷的关系

设导体表面电荷面密度为 $\sigma(x,y,z)$，设 $P$ 是导体外紧靠导体表面的一点，相关的电场强度为 $\mathbf{E}_{\text{表}}(x,y,z)$。确定电场强度 $\mathbf{E}$ 和电荷密度 $\sigma$ 的关系：

\[
\oint_S \mathbf{E} \cdot d\mathbf{S} = \mathbf{E}_{\text{表}} \cdot d\mathbf{S} = \frac{\sigma}{\varepsilon_0} d\mathbf{S}
\]

$\vec{n}$ 为导体外法线方向。

**注意：上式中的电场是合场强。**

--- PAGE 006 ---
# 电极化强度矢量

描述电介质在电场中极化强弱的物理量

(1) **P 的定义**

\[
\vec{P} = \lim_{\Delta V \to 0} \frac{\sum \vec{p}_i}{\Delta V}
\]

单位体积内所有分子的电偶极矩矢量和

单位：库仑/米$^2$ (C/m$^2$)

显然 $\vec{E}_{\text{外}} = 0$ $\sum \vec{p}_i = 0$ $\vec{P} = 0$

(2) 电介质的极化规律：对于各向同性的均匀电介质，其中任一点处的电极化强度矢量与该点的总场强成正比。

\[
\vec{P} = \chi_e \varepsilon_0 \vec{E}
\]

\[
\vec{E} = \vec{E}_{\text{外}} + \vec{E}'
\]

\[
\chi_e = \varepsilon_r - 1
\]

$\chi_e$ —— 电极化率
$\varepsilon_r$ —— 相对介电常数

真空 $\varepsilon_r = 1$
空气 $\varepsilon_r \approx 1$
其他 $\varepsilon_r > 1$

--- PAGE 007 ---
例 已知两杆电荷线密度为 \(\lambda\)，长度为 \(L\)，相距 \(L\)

求 两带电直杆间的电场力。

解 \(dq = \lambda dx\)

\(dq' = \lambda dx'\)

\[
\mathrm{d}F = \frac{\lambda \mathrm{d}x \cdot \lambda \mathrm{d}x'}{4\pi\varepsilon_0 (x' - x)^2}
\]

\[
F = \int_{2L}^{3L} \mathrm{d}x' \int_{0}^{L} \frac{\lambda^2 \mathrm{d}x}{4\pi\varepsilon_0 (x' - x)^2}
= \frac{\lambda^2}{4\pi\varepsilon_0} \ln \frac{4}{3}
\]

--- PAGE 007 ---
例 如图所示,在带电量为Q的点电荷所产生的静电场中,有一带电量为q的点电荷

**求**: q在a点和b点的电势能

解: 选无穷远为电势能零点

\[ W_a = \int_a^\infty q \vec{E} \cdot d\vec{l} = \frac{qQ}{4\pi \epsilon_0 r_a} \]

\[ W_b = \int_b^\infty q \vec{E} \cdot d\vec{l} = \frac{qQ}{4\pi \epsilon_0 r_b} \]

选 C 点为电势能零点

\[ W_a = \int_a^c q\vec{E} \cdot d\vec{l} = \frac{qQ}{4\pi \epsilon_0} \left( \frac{1}{r_a} - \frac{1}{r_c} \right) \]

\[ W_b = \int_c^b q\vec{E} \cdot d\vec{l} = \frac{qQ}{4\pi \epsilon_0} \left( \frac{1}{r_b} - \frac{1}{r_c} \right) \]

两点的电势能差：\(W_a - W_b = \int_a^b q\vec{E} \cdot d\vec{l} = \frac{qQ}{4\pi \epsilon_0} \left( \frac{1}{r_a} - \frac{1}{r_b} \right)\)

--- PAGE 007 ---
## 3. 处于静电平衡的孤立带电导体电荷分布

由实验可得以下定性的结论：

\[
\sigma \propto \frac{1}{R}
\]

**尖端放电** (危害、应用)

## 4. 静电屏蔽

- 如果空腔中无电荷，则导体带电只能在表面。
- 如果空腔中有电荷，则导体带电只能在表面。

\[
E_{\text{表}} = \frac{\sigma}{\varepsilon_0}
\]

--- PAGE 007 ---
# 电极化强度矢量与极化电荷的关系：

设在均匀电介质中截取一斜柱体，体积为 $\Delta V$。

\[
\Delta V = \Delta S \cdot l \cos \theta
\]

\[
\sum \vec{p}_i = \sigma' \Delta S \vec{l} = q' \vec{l}
\]

\[
|\vec{P}| = \frac{\sum \vec{p}_i}{\Delta V} = \frac{\sigma' \cdot \Delta S \cdot l}{\Delta S \cdot l \cos \theta} = \frac{\sigma'}{\cos \theta}
\]

\[
\sigma' = |\vec{P}| \cdot \cos \theta = P_n
\]

均匀电介质表面产生的极化电荷面密度等于该处电极化强度沿表面外法线方向的投影。

--- PAGE 008 ---
## 9.2 静电场 电场强度 \(\vec{E}\)

### 一. 静电场

接触力 —— 近距离作用

非接触力 —— 超距作用，无需作用时间

- 早期：电磁理论是超距作用和"以太"理论
- 后来：法拉第提出场（力线）的概念

电磁场是物质的一种形态，它可以脱离电荷和电流独立存在，具有能量、动量和角动量等物质的基本属性。它在真空中以光速传播。

- 电场的特点
  (1) 对位于其中的带电体有力的作用——力
  (2) 带电体在电场中运动，电场力要作功——能量

*(此处有插图)*

--- PAGE 008 ---
9.5 电势 电势差

一. 电势 电势差

单位正电荷自\(a \to b\)过程中电场力作的功。

· 电势差

\[u_{ab} = \frac{W_a - W_b}{q_0} = \frac{A_{ab}}{q_0} = \int_a^b \vec{E} \cdot d\vec{l}\]

单位正电荷自该点 \(\to\) "势能零点" 过程中电场力作的功。

· 电势定义

\[u_a = \frac{W_a}{q_0}\]

\[u_a = \frac{A_{a\to 0}}{q_0} = \int_a^{0} \vec{E} \cdot d\vec{l}\]

--- PAGE 008 ---
## • 静电屏蔽

腔内、腔外的场互不影响。

--- PAGE 008 ---
# 三.电介质的高斯定理 电位移矢量

真空中的高斯定理：

\[
\oint_S \vec{E} \cdot d\vec{S} = \frac{1}{\varepsilon_0} \sum q_i
\]

介质中的高斯定理：

\[
\oint_S \vec{E} \cdot d\vec{S} = \frac{1}{\varepsilon_0} \left(\sum q_i + \sum q'_i\right)
\]

以导体平板为例：

\[
\begin{align*}
\oint_S \vec{P} \cdot d\vec{S} &= \int_{S'} \vec{P} \cdot d\vec{S} \\
&= \int_{S'} \sigma' dS \\
&= -\sum q'_i
\end{align*}
\]

--- PAGE 009 ---
### 二. 电场强度

电场对位于其中的带电体有力的作用，从电场力的性质出发来定量地描述电场，引入电场强度矢量的概念。

#### 试探电荷

为了定量研究电场，在电场中引入试探点电荷：

- 电量充分小，以不改变被研究物体的电荷或电场分布；
- 线度充分小，本身无电荷空间分布，即点电荷。

试探电荷所受的力的大小和方向只与其所在的位置有关，与试探电荷大小、正负无关，这个矢量反映电场中空间各个确定的点本身的性质。

**定义**：电场中某点的电场强度的大小等于单位电荷在该点受力的大小，其方向为正电荷在该点受力的方向。

\[
\vec{E} = \frac{\vec{F}}{q_0}
\]

--- PAGE 009 ---
• 点电荷的电势

\[
u_a = \int_a^{\infty} \vec{E} \cdot d\vec{l} \quad \vec{E} = \frac{q}{4\pi\varepsilon_0} \frac{1}{r^2} \hat{r} \quad d\vec{l} = dr \hat{r}
\]

\[
u_a = \frac{q}{4\pi\varepsilon_0} \int_r^\infty \frac{dr}{r^2} = \frac{q}{4\pi\varepsilon_0 r}
\]

## 二. 电势叠加原理

• 点电荷系的电势

\[
u_p = \int_p^{\infty} \vec{E} \cdot d\vec{l}
\]

\[
\begin{align*}
&= \int_p^{\infty} (\vec{E}_1 + \vec{E}_2) \cdot d\vec{l} \\
&= \int_{r_1}^{\infty} \frac{q_1}{4\pi\varepsilon_0 r_1^2} dr + \int_{r_2}^{\infty} \frac{q_2}{4\pi\varepsilon_0 r_2^2} dr \\
&= \frac{q_1}{4\pi\varepsilon_0 r_1} + \frac{q_2}{4\pi\varepsilon_0 r_2}
\end{align*}
\]

--- PAGE 009 ---
**例1** 两块等面积的金属平板，分别带电荷 $q_A$ 和 $q_B$，平板面积均为 $S$，两板间距离为 $d$，且满足面积的线度远大于 $d$。

求：静电平衡时两金属板各表面上的电荷面密度。

解：如图示，设4个表面的电荷面密度分别为 $\sigma_1$、$\sigma_2$、$\sigma_3$ 和 $\sigma_4$，由电荷守恒，得

\[
\sigma_1 S + \sigma_2 S = q_A, \quad \sigma_3 S + \sigma_4 S = q_B
\]

在两板内分别取任意两点 A 和 B，则

\[
\begin{aligned}
E_A &= \frac{\sigma_1}{2\varepsilon_0} - \frac{\sigma_2}{2\varepsilon_0} - \frac{\sigma_3}{2\varepsilon_0} - \frac{\sigma_4}{2\varepsilon_0} = 0 \\[0.5em]
E_B &= \frac{\sigma_1}{2\varepsilon_0} + \frac{\sigma_2}{2\varepsilon_0} + \frac{\sigma_3}{2\varepsilon_0} - \frac{\sigma_4}{2\varepsilon_0} = 0
\end{aligned}
\]

解得

\[
\sigma_1 = \sigma_4, \quad \sigma_2 = -\sigma_3
\]

--- PAGE 009 ---
\[
\oint_{S} \vec{E} \cdot d\vec{S} = \frac{1}{\varepsilon_0} \sum q_i - \frac{1}{\varepsilon_0} \oint_{S} \vec{P} \cdot d\vec{S}
\]

\[
\oint_{S} \left( \varepsilon_0 \vec{E} + \vec{P} \right) \cdot d\vec{S} = \sum q_i
\]

定义电位移矢量：

\[
\vec{D} = \varepsilon_0 \vec{E} + \vec{P} \quad \text{C} \cdot \text{m}^{-2}
\]

**高斯定理的普通积分形式：**

\[
\oint_{S} \vec{D} \cdot d\vec{S} = \int_{V} \rho dV = \sum q_i
\]

**微分形式：**

\[
\nabla \cdot \vec{D} = \rho
\]

**高斯定理的一般表述：** 通过高斯面的电位移通量等于高斯面所包围的自由电荷的代数和，与极化电荷及高斯面外电荷无关。

它对于所有宏观电磁现象是普遍成立的。

--- PAGE 010 ---
电场强度的单位是 V/m 或 N/C

电场是时空坐标的函数，本章讨论静电场，故：

\[
\frac{\partial \vec{E}(x, y, z, t)}{\partial t} = 0
\]

仅为**空间坐标的函数**：

\[
\vec{E} = \vec{E}(x, y, z)
\]

在静电场中，任一点只有一个电场强度与之对应，即静电场具有**单位性**。

因此，产生电场的电荷分布已知时，空间中任意一点的电场就能被唯一地确定下来，这是静电学的经典问题。

--- PAGE 010 ---
对n个点电荷

\[u = \sum_{i=1}^{n} \frac{q_i}{4\pi \varepsilon_0 r_i}\]

在点电荷系产生的电场中, 某点的电势是各个点电荷单独存在时, 在该点产生的电势的代数和。这称为电势叠加原理。

对连续分布的带电体

\[u = \int \frac{dq}{4\pi\varepsilon_0 r}\]

三. 电势的计算

\[
\begin{cases}
\text{(1) 已知电荷分布} & u = \int \frac{dq}{4\pi\varepsilon_0 r} \\
\text{方法} \\
\text{(2) 已知场强分布} & u_p = \int_p \vec{E} \cdot \mathrm{d}\vec{l}
\end{cases}
\]

--- PAGE 010 ---
代入①，得

\[
\sigma_1 = \sigma_4 = \frac{q_A + q_B}{2S}
\]

\[
\sigma_2 = -\sigma_3 = \frac{q_A - q_B}{2S}
\]

可见，A、B两板的内侧面带等量异号电荷；两板的外侧面带等量同号电荷。

特别地，若 $q_A = -q_B = q$，则

\[
\sigma_1 = \sigma_4 = 0, \quad \sigma_2 = -\sigma_3 = \frac{q}{S}
\]

电荷只分布在两板的内侧面，外侧面不带电。

--- PAGE 010 ---
- 比较

\[
\begin{aligned}
\oint_S \vec{D} \cdot d\vec{S} &= \sum_i q_{0i,\text{自由}} \\
\oint_S \vec{E} \cdot d\vec{S} &= \frac{1}{\varepsilon_0} \left( \sum q_{0i,\text{自由}} + \sum q_{i,\text{极化}} \right)
\end{aligned}
\]

1. 由于极化电荷与外场有关，极化电荷密度和极化强度 P 并不容易求出，因此引入 D 后，高斯定理的形式不再考虑极化电荷，依然只考虑自由电荷。以上两个方程是完全等价的。

2. 介质中的高斯定理包含了真空中的高斯定理。

\[
\vec{P} = 0 \quad \text{所以:} \quad \vec{D} = \varepsilon_0 \vec{E} + \vec{P} = \varepsilon_0 \vec{E}
\]

\[
\oint_{\mathcal{S}} \vec{D} \cdot d\vec{S} = \oint_{\mathcal{S}} \varepsilon_0 \vec{E} \cdot d\vec{S} = \sum q_i \qquad \oint_{\mathcal{S}} \vec{E} \cdot d\vec{S} = \frac{1}{\varepsilon_0} \sum q_i
\]

3. 描写电场的基本物理量是 E，而 D 是一个辅助量。

--- PAGE 011 ---
### 三. 电场强度叠加原理

点电荷的电场

\[
\vec{F} = \frac{1}{4\pi\varepsilon_0} \frac{qq_0}{r^2} \hat{r}^0
\]

\[
\vec{E} = \frac{\vec{F}}{q_0} = \frac{1}{4\pi\varepsilon_0} \frac{q}{r^2} \hat{r}^0
\]

点电荷系的电场

\[
\vec{E} = \sum_k \vec{E}_k = \sum_k \left( \frac{1}{4\pi\varepsilon_0} \frac{q_k}{r_k^2} \hat{r}_k^0 \right)
\]

点电荷系在某点 P 产生的电场强度等于各点电荷单独在该点产生的电场强度的矢量和。这称为**电场强度叠加原理**。

*(此处有插图)*

--- PAGE 011 ---
## 书中例题8.15(p.314)

求均匀电场中任一点的电势及任意两点间的电势差。

解：均匀电场方向为x方向，沿x轴方向运动作功，沿y轴方向运动不作功，两点间的电势差为：

\[u_a - u_b = \int_a^b \vec{E} \cdot d\vec{l} = \int_a^b Edx = E(x_b - x_a)\]

选x=0处的电势为u₀，则空间任意一点的电势为：

\[ \begin{aligned} u_x - u_0 &= \int_x^0 E dx = E(0 - x) \\ u_x &= u_0 - E x \end{aligned} \]

电势沿x方向线性减小。

--- PAGE 011 ---
**例2** 半径为 $R_1$ 的导体球带有电荷 $q$，球外有一个内、外半径为 $R_2$、$R_3$ 的同心导体球壳，壳上带有电量为 $Q$，如图所示，求：

(1) 两球的电势 $V_1$ 和 $V_2$，

(2) 两球的电势差 $\Delta V = V_1 - V_2$

(3) 用导线把球和球壳联在一起后，$V_1$ 和 $V_2$ 及 $\Delta V$ 分别是多少

(4) 在情形(1)、(2)中，若外球接地，$V_1$ 和 $V_2$ 及 $\Delta V$ 分别是多少？

(5) 设外球离地面很远，若内球接地，$V_1$、$V_2$、$\Delta V$ 各为多少？

--- PAGE 011 ---
对于各向同性的电介质：$\vec{P} = \chi_e \varepsilon_0 \vec{E}$

\[
\vec{D} = (\varepsilon_0 \vec{E} + \vec{P}) = \varepsilon_0 \vec{E} + \chi_e \varepsilon_0 \vec{E} = (1 + \chi_e) \varepsilon_0 \vec{E}
\]

\[
\begin{align*}
\varepsilon_r &= 1 + \chi_e \quad \varepsilon_r \text{称为：相对介电常量} \\
\vec{D} &= \varepsilon_0 \varepsilon_r \vec{E} \quad \varepsilon \text{称为：介电常量}
\end{align*}
\]

\[
\boxed{\vec{D} = \varepsilon \vec{E}}
\]

D 和 E 是两个不同物理意义矢量。在各向同性介质中 D 和 E 方向相同，而各向异性介质中 D 和 E 的方向不同。

**注意:** $\vec{D} = \varepsilon_0 \vec{E} + \vec{P}$ 是定义式，普遍成立。

$\vec{D} = \varepsilon \vec{E}$ 只适用于各向同性的均匀介质。

--- PAGE 012 ---
例 求电偶极子在延长线上和中垂线上一点产生的电场强度。

一对靠的很近的等量异号电荷构成带电体系，这样的模型称为**电偶极子**。

解

\[
E_+ = \frac{q}{4\pi\varepsilon_0 (x - l/2)^2} i, \quad
E_- = -\frac{q}{4\pi\varepsilon_0 (x + l/2)^2} i
\]

\[
E = E_+ + E_- = \frac{q \cdot 2xl}{4\pi\varepsilon_0 (x^2 - l^2/4)^2} i
\]

电偶极矩 \(\vec{p} = q\vec{l}\)

\[
= \frac{2x\vec{p}}{4\pi\varepsilon_0 (x^2 - l^2/4)^2}
\]

电偶极矩是描述电偶极子属性的物理量，只与异号电荷的电量和它们距离的乘积有关，它是矢量，方向是负电荷指向正电荷的方向。

*(此处有插图)*

--- PAGE 012 ---
# 电偶极子在均强电场中的电势能

选x=0处电势为u₀，由 u_x = u₀ - Ex

电荷+q的电势能为

\[
W_+ = q u_+ = q[u_0 - E(x_0 + l \cos \theta)]
\]

电荷-q的电势能为

\[
W_- = -q u_- = -q[u_0 - Ex_0]
\]

总电势能为

\[
\begin{align*}
W &= W_+ + W_- = q[u_0 - E(x_0 + l \cos \theta)] - q[u_0 - Ex_0] \\
&= -qlE \cos \theta = -\vec{p} \cdot \vec{E}
\end{align*}
\]

- 在均匀电场中，电偶极子的电势能与其位置无关，而与它相对于电场方向的指向有关。

- 当电偶极矩矢量与电场方向相同时，电势能为-pE，处于势能的最小值，处于稳定平衡状态。

--- PAGE 012 ---
解：(1) 各球面所带的电荷：

由于静电感应，静电平衡时电荷分布

- 导体球表面：$q$
- 导体球壳：$\begin{cases} \text{内表面：} -q \\ \text{外表面：} Q+q \end{cases}$ (电荷守恒)

(2) 先用高斯定理求场强分布，再用积分求电势。

\[
E = \begin{cases}
0 & (r < R_1) \\[0.3em]
\displaystyle \frac{q}{4\pi\varepsilon_0 r^2} & (R_1 < r < R_2) \\[0.6em]
0 & (R_2 < r < R_3) \\[0.3em]
\displaystyle \frac{Q+q}{4\pi\varepsilon_0 r^2} & (r > R_3)
\end{cases}
\]

--- PAGE 012 ---
# 静电场环路定理的一般形式

束缚电荷 $q_{\text{束}}$ 产生的电场与自由电荷 $q_{\text{自}}$ 产生的电场相同 —— 保守力场

则有

\[
\oint_L \vec{E} \cdot d\vec{l} = 0 \quad \text{——电介质中的环路定理}
\]

## 总结

(1) 四个常数之间的关系

\[
\begin{array}{l}
\text{介质介电常数} \; \varepsilon = \varepsilon_r \varepsilon_0 \\
\text{相对介电常数} \; \varepsilon_r = 1 + \chi_e
\end{array}
\]

(2) 三个物理量 $\vec{E}, \vec{P}, \vec{D}$ 之间的关系

\[
\begin{cases}
\vec{P} = \chi_e \varepsilon_0 \vec{E} \\
\vec{D} = \varepsilon_r \varepsilon_0 \vec{E}
\end{cases}, \qquad \vec{D} = \varepsilon_0 \vec{E} + \vec{P}
\]

(3) 解题一般步骤

\[
\begin{cases}
\vec{E} = \dfrac{\vec{D}}{\varepsilon} \\
\vec{P} = \chi_e \varepsilon_0 \vec{E}
\end{cases}
\]

--- PAGE 013 ---
在中垂线上 \(E_+ = E_- = \frac{q}{4\pi\varepsilon_0 (r^2 + l^2/4)}\)

\[
E = E_x = 2E_+ \cos\theta, \quad E_y = 0
\]

\[
\cos\theta = \frac{l/2}{\sqrt{r^2 + l^2/4}}, \quad
E = 2E_+ \cos\theta = \frac{1}{4\pi\varepsilon_0} \frac{ql}{(r^2 + l^2/4)^{3/2}}
\]

若电荷间的距离 \(l\) 远比到场点的距离 \(r\) 小，即 \(r \gg l\) 时

\[
\frac{2xl}{(x^2 - l^2/4)^2} \approx \frac{2l}{r^3}, \quad
\frac{l}{(r^2 + l^2/4)^{3/2}} \approx \frac{l}{r^3}
\]

延长线上电场为
\[
E = \frac{2\vec{p}}{4\pi\varepsilon_0 r^3}
\]

中垂线上电场为
\[
E = -\frac{\vec{p}}{4\pi\varepsilon_0 r^3}
\]

电偶极子的场强与距离 \(r\) 的三次方成反比，比点电荷随 \(r\) 递减的速度要快得多。

*(此处有插图)*

--- PAGE 013 ---
# 电偶极子的电势

取无穷远处为电势零点，根据电势叠加原理：

\[u_+ = \frac{1}{4\pi\varepsilon_0}\frac{q}{r_+}, \quad u_- = \frac{1}{4\pi\varepsilon_0}\frac{q}{r_-}\]

\[u = u_+ + u_- = \frac{q}{4\pi\varepsilon_0}\left(\frac{1}{r_+} - \frac{1}{r_-}\right) = \frac{q}{4\pi\varepsilon_0}\left(\frac{r_- - r_+}{r_+ r_-}\right)\]

\(r \gg l\)，所以 \(r_+ r_- \approx r^2\)，\(r_- - r_+ \approx l \cos \theta\)，其中 \(\theta\) 为 \(r\) 与 \(l\) 之间的夹角

\[u_p = \frac{ql}{4\pi\varepsilon_0} \frac{\cos \theta}{r^2}\]

用 \(\vec{r}\) 表示P点相对于电偶极子的位矢

\[u_p = \frac{1}{4\pi\varepsilon_0} \frac{\vec{p} \cdot \vec{r}}{r^3}\]

--- PAGE 013 ---
导体球的电势 $V_1$

\[
V_1 = \int_{R_1}^{\infty} \vec{E} \cdot d\vec{l}
= \int_{R_1}^{R_2} \vec{E} \cdot d\vec{r} + \int_{R_2}^{R_3} \vec{E} \cdot d\vec{r} + \int_{R_3}^{\infty} \vec{E} \cdot d\vec{r}
\]

\[
= \int_{R_1}^{R_2} \frac{q}{4\pi\varepsilon_0 r^2} dr + \int_{R_2}^{R_3} 0 \, dr + \int_{R_3}^{\infty} \frac{Q+q}{4\pi\varepsilon_0 r^2} dr
\]

\[
= \frac{1}{4\pi\varepsilon_0} \left( \frac{q}{R_1} - \frac{q}{R_2} \right) + \frac{1}{4\pi\varepsilon_0} \frac{Q+q}{R_3}
\]

导体球壳的电势 $V_2$

\[
V_2 = \int_{R_3}^{\infty} E \cdot dr = \int_{R_3}^{\infty} \frac{Q+q}{4\pi\varepsilon_0 r^2} dr = \frac{1}{4\pi\varepsilon_0} \frac{Q+q}{R_3}
\]

--- PAGE 013 ---
## 教材例题8.36(p.346) 重点

例 平行板电容器，其中充有两种均匀电介质。

求 (1) 各电介质层中的场强

(2) 极板间电势差和电容

解 做一个圆柱形高斯面 $S_1$

\[
\oint_S \vec{D} \cdot d\vec{S} = \sum q_i (S_1 \text{内}) \quad D_1 \Delta S_1 = \sigma_0 \Delta S_1
\]

\[
D_1 = \sigma_0 \qquad E_1 = \frac{D_1}{\varepsilon_0 \varepsilon_{r1}} = \frac{\sigma_0}{\varepsilon_0 \varepsilon_{r1}}
\]

同理，做一个圆柱形高斯面 $S_2$

\[
\oint_{S_2} \vec{D} \cdot d\vec{S} = \sum q_i (S_2 \text{内}) \quad D_2 = \sigma_0 \qquad E_2 = \frac{D_2}{\varepsilon_0 \varepsilon_{r2}} = \frac{\sigma_0}{\varepsilon_0 \varepsilon_{r2}}
\]

\[
D_1 = D_2 \qquad E_1 \neq E_2
\]

--- PAGE 014 ---
连续分布带电体

\[
d\vec{E} = \frac{1}{4\pi\varepsilon_0} \frac{dq}{r^2} \hat{r}^0
\]

\[
\vec{E} = \int \frac{dq}{4\pi\varepsilon_0 r^2} \hat{r}^0
\]

\[
dq = 
\begin{cases}
\lambda \, dl & (\text{线分布}) \\
\sigma \, dS & (\text{面分布}) \\
\rho \, dV & (\text{体分布})
\end{cases}
\]

\(\lambda\)：线密度，\(\sigma\)：面密度，\(\rho\)：体密度

**积分求连续分布带电体的电场是本课程的重点！**

*(此处有插图)*

--- PAGE 014 ---
# 书中例题8.18(p.316) 重点

例 均匀带电圆环半径为 \(R\)，电荷线密度为 \(\lambda\)。

求 圆环轴线上一点的电势

解 建立如图坐标系，选取电荷元 \(dq\)

\[dq = \lambda dl\]

\[du = \frac{dq}{4\pi \epsilon_0 r} = \frac{\lambda dl}{4\pi \epsilon_0 \sqrt{R^2 + x^2}}\]

\[u_p = \int_0^{2\pi R} \frac{\lambda dl}{4\pi \epsilon_0 \sqrt{R^2 + x^2}} = \frac{2\pi R\lambda}{4\pi \epsilon_0 \sqrt{R^2+x^2}}\]

--- PAGE 014 ---
**方法二：电势叠加法：**

导体组可看成三层均匀带电球面

\[
V_1 = \frac{q}{4\pi\varepsilon_0 R_1} + \frac{-q}{4\pi\varepsilon_0 R_2} + \frac{Q+q}{4\pi\varepsilon_0 R_3}
\]

\[
V_2 = \frac{q}{4\pi\varepsilon_0 R_3} + \frac{-q}{4\pi\varepsilon_0 R_3} + \frac{Q+q}{4\pi\varepsilon_0 R_3} = \frac{1}{4\pi\varepsilon_0} \frac{Q+q}{R_3}
\]

(2) 两球的电势差：

\[
\Delta V = V_1 - V_2 = \frac{1}{4\pi\varepsilon_0} \left( \frac{q}{R_1} - \frac{q}{R_2} \right)
\]

--- PAGE 014 ---
\[
\Delta u = \int_A^B \vec{E} \cdot d\vec{r} = \int_0^{d_1} \vec{E}_1 \cdot d\vec{r} + \int_{d_1}^{d_1 + d_2} \vec{E}_2 \cdot d\vec{r}
\]

\[
= \frac{\sigma}{\varepsilon_0 \varepsilon_{r1}} d_1 + \frac{\sigma}{\varepsilon_0 \varepsilon_{r2}} d_2
\]

\[
C = q / \Delta u = \frac{\varepsilon_1 \varepsilon_{2} S}{\varepsilon_1 d_2 + \varepsilon_2 d_1}
\]

- 各电介质层中的场强不同，电位移相同
- 相当于电容器的串联

--- PAGE 015 ---
例 半径为 \(R\) 的均匀带电细圆环，带电量为 \(q\)

求 圆环轴线上任一点 \(P\) 的电场强度

解 \(dq = \lambda dl\)

\[
d\vec{E} = \frac{1}{4\pi\varepsilon_0} \frac{dq}{r^2} \hat{r}^0
\]

\[
\vec{E} = \int d\vec{E} = \int \frac{1}{4\pi\varepsilon_0} \frac{dq}{r^2} \hat{r}^0
\]

\[
d\vec{E}_\perp = d\vec{E} \sin\theta, \quad d\vec{E}_x = d\vec{E} \cos\theta
\]

圆环上电荷分布关于 \(x\) 轴对称 \(\Rightarrow E_\perp = 0\)

\[
E_x = \frac{1}{4\pi\varepsilon_0} \int \frac{dq}{r^2} \cos\theta
= \frac{1}{4\pi\varepsilon_0} \frac{\cos\theta}{r^2} \int dq
= \frac{1}{4\pi\varepsilon_0} \frac{q}{r^2} \cos\theta
\]

\[
\cos\theta = \frac{x}{r}, \quad r = (R^2 + x^2)^{1/2}
\]

\[
E = \frac{1}{4\pi\varepsilon_0} \frac{qx}{(R^2 + x^2)^{3/2}}
\]

*(此处有插图)*

--- PAGE 015 ---
## 书中例题8.19(p.316)

计算半径为R，均匀带电量为q的圆形平面板轴线上任意一点的电势。

解：把圆盘分割成无穷多个半径不同的同心细圆环，每个圆环在轴上产生的电场强度都可应用前一例题的结果，这时细圆环所带的电量相对整个圆盘来说是 \(dq = \sigma 2\pi r dr\)，其中 \(\sigma = q/\pi R^2\) 是圆盘的面电荷密度。\(dq\) 在P点产生的电势为：

\[du = \frac{1}{4\pi \varepsilon_0} \frac{dq}{(r^2 + x^2)^{\frac{1}{2}}} = \frac{1}{4\pi \varepsilon_0} \frac{\sigma 2\pi r dr}{(r^2 + x^2)^{\frac{1}{2}}}\]

从0到R积分，即得圆盘在P点的电势：

\[
u_p = \int du = \int_0^R \frac{\sigma 2\pi r dr}{4\pi \varepsilon_0 (r^2 + x^2)^{\frac{1}{2}}} = \frac{\sigma}{2\varepsilon_0} \int_0^R \frac{r dr}{(r^2 + x^2)^{\frac{1}{2}}}
= \frac{\sigma}{2\varepsilon_0} \sqrt{r^2 + x^2} \bigg|_0^R = \frac{\sigma}{2\varepsilon_0} \left(\sqrt{R^2 + x^2} - x\right)
\]

以上两例题都是由点电荷的电位经过积分得出空间的电位分布。

--- PAGE 015 ---
(3) 用导线连接两球，电荷重新分布：

- 导体球表面：$0$
- 导体球壳：$\begin{cases} \text{内表面：} 0 \\ \text{外表面：} Q+q \end{cases}$

\[
V_1 = V_2 = \frac{Q+q}{4\pi\varepsilon_0 R_3}, \quad \Delta V = 0
\]

(4) 导体球壳接地，电荷重新分布：

- 导体球表面：$q$
- 导体球壳：$\begin{cases} \text{内表面：} -q \\ \text{外表面：} 0 \end{cases}$

\[
V_1 = \frac{q}{4\pi\varepsilon_0 R_1} + \frac{-q}{4\pi\varepsilon_0 R_2}, \quad V_2 = 0, \quad \Delta V = V_1
\]

--- PAGE 015 ---
# 平板电容器中充介质的另一种情况

平行板电容器面积 S，间距 d，带电量为 Q。一半充有电容率 $\varepsilon_{r1}$ 的电介质，另一半充有电容率 $\varepsilon_{r2}$ 的电介质。

求：(1) 介质中任意点的电场强度和电位移矢量；(2) 电容器的电容。

解：由极板内为等势体 $\Delta u_1 = \Delta u_2$

\[
E_1 = \frac{\Delta u_1}{d} \quad E_2 = \frac{\Delta u_2}{d}
\]

极板间各处的电场强度相同。

由于电介质不同，极化电荷数量不同，造成自由电荷分布密度不同，由此造成电位移不同。

--- PAGE 016 ---
讨论

(1) 当 \(x = 0\)（即 \(P\) 点在圆环中心处）时，
\[
E = 0
\]

(2) 当 \(x \gg R\) 时，
\[
E = \frac{1}{4\pi\varepsilon_0} \frac{q}{x^2}
\]
可以把带电圆环视为一个点电荷

*(此处有 Ex-R 关系图)*

--- PAGE 016 ---
对于有对称性的物体可由高斯定理求出电场，再由电场积分得到电势

书中例题8.21 (p.319)

半径为R，带电量为q的均匀带电球面的电分布。

试求：球外任意一点产生的电势。

解：由高斯定理求出电场强度的分布：

\[E = 0 \quad (r < R)\]

\[E = \frac{1}{4\pi\epsilon_0} \frac{q}{r^2} \quad (r > R)\]

当r≥R时，电势为：

\[u_p = \int_P^\infty \vec{E} \cdot d\vec{l} = \int_r^\infty \frac{1}{4\pi\epsilon_0} \frac{q}{r^2} dr = \frac{1}{4\pi\epsilon_0} \frac{q}{r}\]

当r<R时，电势为：

\[u_p = \int_P^\infty \vec{E} \cdot d\vec{l} = \left( \int_{P}^{R} \vec{E} \cdot d\vec{l} + \int_{R}^{\infty} \vec{E} \cdot d\vec{l} \right)\]

在球面内（r<R），\(E=0\)，上式第一项积分为0，所以

\[u_p = \int_R^\infty \vec{E} \cdot d\vec{l} = \int_R^\infty \frac{1}{4\pi\epsilon_0} \frac{q}{r^2} dr = \frac{1}{4\pi\epsilon_0} \frac{q}{R}\]

--- PAGE 016 ---
(5) 内球接地，$V_1=0$，电荷重新分布：

- 导体球表面：$q'$
- 导体球壳：$\begin{cases} \text{内表面：} -q' \\ \text{外表面：} Q+q' \end{cases}$

\[
V_1 = \frac{q'}{4\pi\varepsilon_0 R_1} + \frac{-q'}{4\pi\varepsilon_0 R_2} + \frac{Q+q'}{4\pi\varepsilon_0 R_3} = 0
\]

得：

\[
\begin{aligned}
q' &= \frac{-Q R_1 R_2}{R_1 R_2 + (R_2 - R_1)R_3} \\[0.5em]
V_2 &= \frac{1}{4\pi\varepsilon_0} \frac{Q(R_2 - R_1)}{R_1 R_2 + (R_2 - R_1)R_3} \\[0.5em]
\Delta V &= V_1 - V_2 = -V_2
\end{aligned}
\]

--- PAGE 016 ---
取一个覆盖整个电容器表面的高斯面：

\[
\iiint \vec{D} \cdot d\vec{S} = D_1 S_1 + D_2 S_2 = Q \quad (D_1 + D_2) \frac{S}{2} = Q
\]

\[
D_1 = \varepsilon_0 \varepsilon_{r1} E_1 = \varepsilon_0 \varepsilon_{r1} E
\]

\[
D_2 = \varepsilon_0 \varepsilon_{r2} E_2 = \varepsilon_0 \varepsilon_{r2} E
\]

\[
(\varepsilon_{r1} + \varepsilon_{r2}) \varepsilon_0 E \frac{S}{2} = Q
\]

\[
E = \frac{2Q}{(\varepsilon_{r1} + \varepsilon_{r2}) \varepsilon_0 S}
\]

\[
\begin{aligned}
U &= \int \vec{E} \cdot d\vec{l} = Ed = \frac{2Qd}{\varepsilon_0 (\varepsilon_{r1} + \varepsilon_{r2}) S} \\
C &= \frac{Q}{U} = \frac{\varepsilon_0 (\varepsilon_{r1} + \varepsilon_{r2}) S}{2d} \\
&= \frac{\varepsilon_0 \varepsilon_{r1} S}{2d} + \frac{\varepsilon_0 \varepsilon_{r2} S}{2d} = C_1 + C_2
\end{aligned}
\]

各电介质层中的场强相同，电位移不同

相当于电容器的并联

--- PAGE 017 ---
例 面密度为 \(\sigma\) 的圆板在轴线上任一点的电场强度

解

\[
dq = 2\pi r dr \cdot \sigma
\]

\[
dE = \frac{1}{4\pi\varepsilon_0} \frac{x dq}{(r^2 + x^2)^{3/2}}
= \frac{x\sigma}{2\varepsilon_0} \frac{r dr}{(r^2 + x^2)^{3/2}}
\]

\[
E = \int dE = \frac{x\sigma}{2\varepsilon_0} \int_0^R \frac{r dr}{(r^2 + x^2)^{3/2}}
= \frac{\sigma}{2\varepsilon_0} \left[1 - \frac{x}{(R^2 + x^2)^{1/2}}\right]
\]

\[
\vec{E} = \frac{q}{2\pi\varepsilon_0 R^2} \left[1 - \frac{x}{(R^2 + x^2)^{1/2}}\right] \hat{i}
\]

*(此处有插图)*

--- PAGE 017 ---
例 半径为R，带电量为 \(q\) 的均匀带电球体

求 带电球体的电势分布

解 根据高斯定律可得：

\[
\begin{cases}
r < R: \quad E_1 = \frac{qr}{4\pi\varepsilon_0 R^3} \\
r \geq R: \quad E_2 = \frac{q}{4\pi\varepsilon_0 r^2}
\end{cases}
\]

对球外一点 \(P\):

\[ u_{\text{外}} = \int_p^\infty \vec{E}_2 \cdot d\vec{r} = \int_r^\infty \frac{qdr}{4\pi\varepsilon_0 r^2} = \frac{q}{4\pi\varepsilon_0 r} \]

对球内一点 \(P_1\):

\[ u_{\text{内}} = \int_{P_1}^{\infty} \vec{E} \cdot d\vec{r} = \int_r^R E_1 \, dr + \int_R^{\infty} E_2 \, dr = \frac{q}{8\pi\varepsilon_0 R^3} (3R^2 - r^2) \]

--- PAGE 017 ---
**例3:** 接地导体球附近有一点电荷，求：导体上的感应电荷。

解：接地导体球：$V=0$

设导体球上的感应电荷为 $q'_{\text{感}}$，导体是等势体，$O$ 点电势=0：

\[
V_O = 0
\]

\[
\therefore V_O = V_{\text{感}} + V_q
\]

\[
\therefore V_O = \frac{q'_{\text{感}}}{4\pi\varepsilon_0 R} + \frac{q}{4\pi\varepsilon_0 d} = 0
\]

得：

\[
q'_{\text{感}} = -\frac{R}{d} q
\]

--- PAGE 017 ---
# 四、电场的边值关系

- 所谓边值关系（或叫边界条件）是指两种材料界面两侧的场满足的物理关系，这种关系当界面两侧材料及其电荷分布（或电势分布）确定后具有唯一性，由电磁场基本定理导出。众多电磁学和光学的重要定理都由边值关系导出，也是求解电磁场分布问题所必须的基本方程之一。

在例1中可以看到，由高斯定理可以导出，当界面垂直于电场时，界面两侧的电位移矢量是连续的，而电场强度矢量是不连续的，它的差值由极化电荷密度来决定。

\[
D_1 = D_2 \quad E_1 \neq E_2
\]

--- PAGE 018 ---
讨论

(1) 当 \(R \gg x\)，圆板可视为无限大薄板

\[
E = \frac{\sigma}{2\varepsilon_0}
\]

(2) 
\[
E_I = E_1 - E_2 = 0
\]
\[
E_{II} = E_1 + E_2 = \frac{\sigma}{\varepsilon_0}
\]
\[
E_{III} = E_1 - E_2 = 0
\]

平行板电容器的理想电场模型

(3) 补偿法

\[
\vec{E} = \vec{E}_{R_2} - \vec{E}_{R_1}
\]

--- PAGE 018 ---
例 8.22 "无限长"均匀带电圆柱面的半径为R，单位长度上带电量为\(\lambda\)，试求其电势分布。

**解** 由于电荷分布的轴对称性，应用高斯定理很容易求出电场强度分布为

\[
E = \begin{cases}
0 & (r < R) \\
\frac{\lambda}{2\pi\epsilon_0 r} & (r > R)
\end{cases}
\]

电场强度方向垂直于带电圆柱面沿径向。

若本题仍选取无限远处为电势零参考点，则由 \(\int_{P}^{\infty} \mathbf{E} \cdot d\mathbf{l}\) 的积分结果，可知各点的电势为无限大，这是没有意义的。一般来说，当电荷分布延伸到无限远时，是不能选取无限远处为电势零参考点的。在本题中，可以选取某一距带电圆柱面轴线为 \(r_0\) 的 \(P_0\) 点为电势零参考点。则相对轴线距离为 \(r\) 一点 \(P\) 处的电势为

当 \(r > R\) 时

\[
u_P = \int_{P}^{P_0} \mathbf{E} \cdot d\mathbf{l} = \int_{P}^{P'} \mathbf{E} \cdot d\mathbf{l} + \int_{P'}^{P_0} \mathbf{E} \cdot d\mathbf{l}
\]

--- PAGE 018 ---
# 三. 孤立导体的电容

孤立导体的电势 $u \propto Q$

\[
C = \frac{Q}{u}
\]

孤立导体的电容，单位：法拉 (F)

电容只与导体的几何因素和介质有关，与导体带电量和电势大小无关。物理意义：导体每升高单位电势所需的电量。

求半径为 $R$ 的孤立导体球的电容：

电势为

\[
u = \frac{Q}{4\pi\varepsilon_0 R}
\]

电容为

\[
C = 4\pi\varepsilon_0 R
\]

--- PAGE 018 ---
更一般的情况，如果这个界面上有自由电荷分布，那么 D 和 E 沿着这个界面的法向分量都不连续的，它们界面两侧的差值分别由自由电荷密度和总电荷密度来决定。为了方便起见，我们只关心自由电荷分布

\[
\vec{n} \cdot (\vec{D}_1 - \vec{D}_2) = D_{n1} - D_{n2} = \sigma
\]

电位移矢量的法向分量是不连续的！

在例 2 中可以看到，由高斯定理可以导出，当界面平行于电场时，界面两侧的电场强度矢量是连续的，而电位移矢量是不连续的，自由电荷和极化电荷的重新分布并不发生在两电介质界面处，而是发生在金属极板和电介质界面处。

--- PAGE 019 ---
例 面密度为 \(\sigma\) 的圆板在轴线上任一点的电场强度

解

\[
dq = 2\pi r dr \cdot \sigma
\]

\[
dE = \frac{1}{4\pi\varepsilon_0} \frac{x dq}{(r^2 + x^2)^{3/2}}
= \frac{x\sigma}{2\varepsilon_0} \frac{r dr}{(r^2 + x^2)^{3/2}}
\]

\[
E = \int dE = \frac{x\sigma}{2\varepsilon_0} \int_0^R \frac{r dr}{(r^2 + x^2)^{3/2}}
= \frac{\sigma}{2\varepsilon_0} \left[1 - \frac{x}{(R^2 + x^2)^{1/2}}\right]
\]

\[
\vec{E} = \frac{q}{2\pi\varepsilon_0 R^2} \left[1 - \frac{x}{(R^2 + x^2)^{1/2}}\right] \hat{i}
\]

*(此处有插图)*

--- PAGE 019 ---
因为 \(PP'\) 和轴线平行，因此与电场强度 \(\mathbf{E}\) 垂直，所以上式第一项积分为零。故

\[
u_p = \int_p^{P_0} \mathbf{E} \cdot d\mathbf{l} = \int_r^{r_0} \frac{\lambda}{2\pi\epsilon_0 r} dr = -\frac{\lambda}{2\pi\epsilon_0} \ln r + \frac{\lambda}{2\pi\epsilon_0} \ln r_0
\]

这一结果可以一般地表示为

\[
u_p = -\frac{\lambda}{2\pi\epsilon_0} \ln r + c
\]

式中 \(c = \frac{\lambda}{2\pi\epsilon_0} \ln r_0\) 为与电势零参考点位置有关的常数。

当 \(r < R\) 时

\[
u_p = \int_r^R \mathbf{E} \cdot d\mathbf{l} + \int_R^{r_0} \mathbf{E} \cdot d\mathbf{l} = 0 + \int_R^{r_0} \frac{\lambda}{2\pi{\epsilon_0}r} dr = -\frac{\lambda}{2\pi\epsilon_0} \ln R + c
\]

可以看出，圆柱面内的电势为一常量。

--- PAGE 019 ---
## 四. 电容器的电容

通常，由彼此绝缘相距很近的两导体构成电容器。
使两导体极板带电 $\pm Q$，两导体极板的电势差

\[
\Delta u \propto Q
\]

\[
\text{电容器的电容} \quad C = \frac{Q}{\Delta u}
\]

--- PAGE 019 ---
\[
\begin{align*}
\vec{n} \cdot (\vec{D}_1 - \vec{D}_2) &= \sigma \\
\vec{n} \times (\vec{E}_1 - \vec{E}_2) &= 0
\end{align*}
\]

更一般的情况，如果这个界面上有自由电荷分布，那么 E 沿着这个界面的切向分量与这个界面电荷分布无关，依然是连续的。因此，

\[
\hat{n} \times (\vec{E}_1 - \vec{E}_2) = E_{t1} - E_{t2} = 0
\]

电场强度矢量的切向分量是连续的！

这是电场的边值关系的普遍表达式，它们与磁场的边值关系一起组成电磁场边值关系，是电磁场理论的重要基本方程。

当界面没有自由电荷分布时，问题简化为对于不连续的分量间的关系，与极化电荷分布有关，可以由界面两侧材料的介电常数来求出。

--- PAGE 020 ---
讨论

(1) 当 \(R \gg x\)，圆板可视为无限大薄板

\[
E = \frac{\sigma}{2\varepsilon_0}
\]

(2) 
\[
E_I = E_1 - E_2 = 0
\]
\[
E_{II} = E_1 + E_2 = \frac{\sigma}{\varepsilon_0}
\]
\[
E_{III} = E_1 - E_2 = 0
\]

平行板电容器的理想电场模型

(3) 补偿法

\[
\vec{E} = \vec{E}_{R_2} - \vec{E}_{R_1}
= \frac{x\sigma}{2\varepsilon_0} \left[ \frac{1}{(R_1^2 + x^2)^{1/2}} - \frac{1}{(R_2^2 + x^2)^{1/2}} \right] \hat{i}
\]

--- PAGE 020 ---
## 9.6 等势面 电势与电场强度的微分关系

## 一. 等势面

电场中电势相等的点连成的面称为等势面。

<center>点电荷</center>
<center>电偶极子</center>

--- PAGE 020 ---
电容器电容的大小取决于极板的形状、大小、相对位置以及极板间介质。

### 电容器电容的计算

\[
Q \xleftarrow{} E \xleftarrow{} \Delta u \xleftarrow{} C = \frac{Q}{\Delta u}
\]

(1) 给电容器充电 $\pm Q$，用高斯定理求 $E$；

(2) 由 $U_{AB} = \displaystyle\int_A^B \vec{E} \cdot d\vec{l}$ 求 $U_{AB}$；

(3) 由定义 $C = Q/U_{AB}$ 计算 $C$。

--- PAGE 020 ---
以上结论的严格导出：

$E, P, D$

由于环路是任意选取的，故有界面两侧电场的切向分量相等：

严格的表示为矢量形式：

\[
\hat{n} \times (E_2 - E_1) = 0
\]

界面上的高斯面 S 非常接近两电介质界面，A 是底面积，柱的侧壁面积很小，积分贡献可以略去。如果界面上没有自由电荷，由高斯定理得到：

\[
\oint_S \mathbf{D} \cdot d\mathbf{s} = \iint_{S_1} \mathbf{D} \cdot d\mathbf{s} + \iint_{S_2} \mathbf{D}' \cdot d\mathbf{s} = 0
\]

\[
\boxed{D \cdot n + D' \cdot (-n) \Big|_A = 0}
\]

\[
D_n = D'_n
\]

如果有自由电荷

\[
\boxed{D_2 \cdot n + D_1 \cdot (-n) \Big|_A = \sigma_f A}
\]

\[
n \cdot (D_2 - D_1) = \sigma_f
\]

--- PAGE 021 ---
*(此页为全页插图，无文字内容)*

--- PAGE 021 ---
<center>带电平板电容器内部</center>
<center>示波管内部的电场</center>

--- PAGE 021 ---
### (1) 平行板电容器

\[
E = \frac{\sigma}{\varepsilon_0}
\]

\[
\Delta u = Ed = \frac{Qd}{S\varepsilon_0}
\]

\[
C = \frac{Q}{\Delta u} = \frac{\varepsilon_0 S}{d}
\]

### (2) 球形电容器

\[
4\pi r^2 E = \frac{Q}{\varepsilon_0} \quad \xrightarrow{} \quad E = \frac{Q}{4\pi\varepsilon_0 r^2}
\]

\[
\Delta u = \int_a^b \vec{E} \cdot d\vec{l} = \frac{Q}{4\pi\varepsilon_0} \left( \frac{1}{R_1} - \frac{1}{R_2} \right)
\]

\[
C = \frac{Q}{\Delta u} = \frac{4\pi\varepsilon_0 R_1 R_2}{R_2 - R_1}
\]

--- PAGE 021 ---
电场线的方向在界面处满足

\[
\frac{\tan \theta_1}{\tan \theta_2} = \frac{E_{1t}}{E_{1n}} \bigg/ \frac{E_{2t}}{E_{2n}} = \frac{E_{2n}}{E_{1n}} = \frac{\varepsilon_1}{\varepsilon_2} = \frac{\varepsilon_{r1}}{\varepsilon_{r2}}
\]

如果界面上没有自由电荷

\[
U_1 - U_2 = \int_1^2 \mathbf{E} \cdot d\mathbf{l} = E_{1n} h + E_{2n} h = E_{1n} h \left(1 + \frac{\varepsilon_1}{\varepsilon_2}\right) \xrightarrow{h \to 0} 0
\]

界面两侧的电势是连续的

--- PAGE 022 ---
补充例题（学习指导 P151, 8.1）
半径为 \(R\) 的均匀带电半球面，面电荷密度为 \(\sigma\)。
求：该半球面球心处的场强。

解法一 在球面上任取一面元 \(dS\)，\(dS = R^2 \sin\alpha d\alpha d\theta\)，此面元所带电量 \(dq = \sigma dS\)。电荷元 \(dq\) 在球心 \(O\) 处所激发的场强 \(dE\) 方向是沿径向的。由对称性可知，合场强沿 \(z\) 轴负方向，所以只需求出电荷元产生的场强在 \(z\) 轴方向上的分量和。电荷元在球心处激发的场强在 \(z\) 轴上的投影为

\[
dE_z = -\frac{dq}{4\pi\varepsilon_0 R^2} \cos\alpha
\]

总场强为

\[
\begin{aligned}
E &= E_z = \int dE_z = -\int \frac{\sigma dS}{4\pi\varepsilon_0 R^2} \cos\alpha \\
&= -\frac{\sigma}{4\pi\varepsilon_0} \int_0^{2\pi} d\theta \int_0^{\frac{\pi}{2}} \sin\alpha \cos\alpha d\alpha \\
&= -\frac{\sigma}{4\varepsilon_0}
\end{aligned}
\]

矢量形式为

\[
\vec{E} = -\frac{\sigma}{4\varepsilon_0} \mathbf{k}
\]

*(此处有插图)*

--- PAGE 022 ---
- 等势面的性质

(1) 电场线与等势面处处正交。

\[dA = q_0 \vec{E} \cdot d\vec{l} = q_0 E \cos \theta dl\]

\[dA = q_0 (u_a - u_b)\]

\[u_a = u_b \quad \rightarrow \quad q_0 E \cos \theta dl = 0\]

\[\cos \theta = 0 \quad \rightarrow \quad \theta = \frac{\pi}{2}\]

沿等势面移动电荷时，电场力所作的功为零。

(2) 规定相邻两等势面间的电势差都相同

\[等势面密 \rightarrow E大\]

\[等势面疏 \rightarrow E小\]

(3) 电场强度的方向总是指向电势降落的方向。

--- PAGE 022 ---
### (3) 柱形电容器

\[
2\pi r h E = \frac{Qh}{\varepsilon_0 l} \quad (R_1 < r < R_2)
\]

\[
E = \frac{Q}{2\pi\varepsilon_0 r l} \quad (R_1 < r < R_2)
\]

\[
\Delta u = \int_{R_1}^{R_2} \frac{Q}{2\pi\varepsilon_0 l r} dr = \frac{Q}{2\pi\varepsilon_0 l} \ln \frac{R_2}{R_1}
\]

\[
C = \frac{Q}{\Delta u} = \frac{2\pi\varepsilon_0 l}{\ln(R_2 / R_1)}
\]

--- PAGE 022 ---
# 书中例题 8.37(p.347) (重点)

半径分别为 $R_1$ 和 $R_3$ 的同心导体球面组成的球形电容器，中间充满相对介电常数为 $\varepsilon_{r1}$ 和 $\varepsilon_{r2}$ 的两层各向同性均匀介质，它们的分界线为 $R_2$ 的同心球面。

求：此电容器的电容。

解：在介质中做同心的球型高斯面。通过球面的电位移通量为：

\[
\iint_S \vec{D} \cdot d\vec{S} = D \cdot 4\pi r^2 = q
\]

\[
\begin{align*}
D &= \frac{q}{4\pi r^2} & \quad \mathbf{D} &= \varepsilon_0 \varepsilon_r \mathbf{E} = \varepsilon \mathbf{E} \\
E_1 &= \frac{D}{\varepsilon_0 \varepsilon_{r1}} = \frac{q}{4\pi \varepsilon_0 \varepsilon_{r1} r^2} & E_2 &= \frac{D}{\varepsilon_0 \varepsilon_{r2}} = \frac{q}{4\pi \varepsilon_0 \varepsilon_{r2} r^2}
\end{align*}
\]

--- PAGE 023 ---
解法二 将半球面视为若干半径不等的平行小圆环。利用均匀带电圆环在其轴线上一点所产生的场强结论计算。

在带电半球面上取一半径为 \(y\) 的带电圆环，其面积 \(dS = 2\pi y dl\)，带电量为 \(dq = \sigma dS = \sigma 2\pi y dl\)，它在 \(O\) 点激发的场强沿 \(z\) 轴负方向，其大小为

\[
dE = \frac{1}{4\pi\varepsilon_0} \frac{b dq}{(b^2 + y^2)^{3/2}}
= \frac{b\sigma 2\pi y dl}{4\pi\varepsilon_0 (b^2 + y^2)^{3/2}}
\]

由图可知：\(b^2 + y^2 = R^2\)，\(b = R\cos\alpha\)，\(y = R\sin\alpha\)，\(dl = R d\alpha\)，所以

\[
dE = \frac{\sigma}{4\pi\varepsilon_0} \cdot \frac{R\cos\alpha \cdot 2\pi R\sin\alpha \cdot R d\alpha}{R^3}
= \frac{\sigma}{2\varepsilon_0} \sin\alpha \cos\alpha d\alpha
\]

\[
E = \int dE = \int_0^{\frac{\pi}{2}} \frac{\sigma}{2\varepsilon_0} \sin\alpha \cos\alpha d\alpha
= \frac{\sigma}{4\varepsilon_0}
\]

矢量形式为

\[
\vec{E} = -\frac{\sigma}{4\varepsilon_0} \mathbf{k}
\]

*(此处有插图)*

--- PAGE 023 ---
# 2. 电势与电场强度的微分关系

取两相邻的等势面

把点电荷 \(q_0\) 从 a 移到 b，电场力作功为

\[
\begin{cases}
dA = q_0 \vec{E} \cdot d\vec{l} = q_0 E \cos \theta dl \\
\quad = q_0 E dn \\
\end{cases}
\]

\[
dA = q_0 [u - (u+du)] = -q_0 du
\]

\[
E \cos \theta dl = Edn = -du \qquad E = -\frac{du}{dn}
\]

任意一场点处电场强度的大小等于沿过该点等势面法线方向上电势的变化率，负号表示电场强度的方向指向电势减小的方向。

--- PAGE 023 ---
## 书中例题 8.32(P.335)

由两个半径为 $a$ 的平行长直导线，轴间距离为 $d \gg a$。线电荷密度分别为 $+\lambda$ 和 $-\lambda$。

求：单位长度平行直导线之间的电容。

解：由高斯定理可求出，直导线在 $P$ 点产生的电场强度大小分别为：

\[
E_{+} = \frac{\lambda}{2\pi\varepsilon_0 x}, \quad E_{-} = \frac{\lambda}{2\pi\varepsilon_0 (d-x)}
\]

--- PAGE 023 ---
两极间的电势差为：

\[
U_{R_1} - U_{R_3} = \int_{R_1}^{R_3} \vec{E} \cdot d\vec{r} = \int_{R_1}^{R_2} \vec{E} \cdot d\vec{r} + \int_{R_2}^{R_3} \vec{E} \cdot d\vec{r}
\]

\[
= \frac{q}{4\pi \varepsilon_0} \left[ \frac{1}{\varepsilon_{r1}} \left( \frac{1}{R_1} - \frac{1}{R_2} \right) + \frac{1}{\varepsilon_{r2}} \left( \frac{1}{R_2} - \frac{1}{R_3} \right) \right]
\]

电容器的电容为：

\[
C = \frac{q}{U_{R_1} - U_{R_3}} = \frac{4\pi \varepsilon_0}{\displaystyle \frac{1}{\varepsilon_{r1}} \left( \frac{1}{R_1} - \frac{1}{R_2} \right) + \frac{1}{\varepsilon_{r2}} \left( \frac{1}{R_2} - \frac{1}{R_3} \right)}
\]

--- PAGE 024 ---
积分求电场的解题思路和方法总结 (P.292)

1. 由给定的电荷分布和所求场点的对称性特征，选择恰当的电荷元和坐标系；

2. 应用点电荷电场强度的计算公式，在选定坐标系中写出某一电荷元 \(dq\) 在场点 \(P\) 的场强；

3. 由场强矢量叠加原理用矢量相加或矢量积分求出总场强：
   1) 把 \(d\vec{E}\) 向各个坐标轴上投影，化矢量积分为各个坐标分量上的标量积分；
   2) 重视对称性分析，可以大大简化计算（球对称、轴对称、镜像对称等等）；
   3) 熟悉各种正交曲线坐标系中，线元、面元和体积元的数学表达形式；
   4) 善于利用已有结论，根据对称性、叠加原理和补偿法等方法简化计算。

--- PAGE 024 ---
另一种理解：

\[
E \cos \theta dl = Edn = -du
\]

\[
E_l dl = -du \quad \rightarrow \quad E_l = -\frac{du}{dl}
\]

电场强度在 \(l\) 方向的投影等于电势沿该方向变化率的负值

\[
dl \geq dn \quad \rightarrow \quad \left|\frac{du}{dl}\right| \leq \left|\frac{du}{dn}\right|
\]

电势沿等势面法线方向的变化率最大

--- PAGE 024 ---
$E_{+}$ 和 $E_{-}$ 的方向一致，所以：

\[
E = \frac{\lambda}{2\pi\varepsilon_0} \left( \frac{1}{x} + \frac{1}{d-x} \right)
\]

\[
u_1 - u_2 = \int_1^2 \vec{E} \cdot d\vec{l} = \int_a^{d-a} \frac{\lambda}{2\pi\varepsilon_0} \left( \frac{1}{x} + \frac{1}{d-x} \right) dx = \frac{\lambda}{\pi\varepsilon_0} \ln \frac{d}{a}
\]

电容器的电容：

\[
C = \frac{q}{u_1 - u_2} = \frac{\pi\varepsilon_0}{\ln(d/a)}
\]

任何导体之间都存在着电容，在电子线路中，这种电容称为分布电容，一般情况下分布电容值很小，可忽略不计，但在高频电路中，需要考虑分布电容。

--- PAGE 024 ---
## 补充例题：（重点）

同心导体球面组成的球形电容器，半径分别为 $R_1$ 和 $R_2$，带电量分别为 $\pm Q$，电容器下半部充有电介质油，相对电容率为 $\varepsilon_r$。

求：(1) 介质中任意点的电场强度和电位移矢量；
（2）电容器的电容。

**解：** 分析：金属球壳是等位体，球壳间距相同，有介质处和无介质处的电场都相同。由于电介质的存在，介质中产生了极化电荷。极化电荷使金属表面的自由电荷产生重新分布，有介质的半个球表面自由电荷密度高一些，没有介质的半个球表面自由电荷密度低一些。

由于电位移只与自由电荷有关，与极化电荷无关，有介质的半个球空间的电位移强一些，没有介质的半个球空间的电位移弱一些。但并不知道两个半球自由电荷是如何重新分布的。只知道整个球面的电荷为 Q。

--- PAGE 025 ---
例 长为 \(L\) 的均匀带电直杆，电荷线密度为 \(\lambda\)

求 它在空间一点 \(P\) 产生的电场强度（\(P\) 点到杆的垂直距离为 \(a\)）

计算 \(dq = \lambda dx\)，其中 \(dE = \frac{1}{4\pi\varepsilon_0} \frac{\lambda dx}{r^2}\)

\[
dE_x = dE \cos\theta, \quad dE_y = dE \sin\theta
\]

\[
x = a \tan(\theta - \frac{\pi}{2}) = -a \cot\theta
\]

\[
dx = a \csc^2\theta d\theta, \quad r^2 = a^2 + x^2 = a^2 \csc^2\theta
\]

\[
dE_x = \frac{\lambda}{4\pi\varepsilon_0 a} \cos\theta d\theta, \quad
dE_y = \frac{\lambda}{4\pi\varepsilon_0 a} \sin\theta d\theta
\]

*(此处有插图)*

--- PAGE 025 ---
## 在直角坐标系中

\[
E_x = -\frac{\partial u}{\partial x} \quad E_y = -\frac{\partial u}{\partial y} \quad E_z = -\frac{\partial u}{\partial z}
\]

\[
\vec{E} = -\nabla u = -\left(\frac{\partial u}{\partial x}\vec{i} + \frac{\partial u}{\partial y}\vec{j} + \frac{\partial u}{\partial z}\vec{k}\right)
\]

某点的电场强度等于该点电势梯度的负值

标量场的梯度是一个矢量场，梯度是标量场在空间各点沿空间各个方向的变化率。

至此我们给出了关于真空中静电场的所有基本概念：

• 库伦定律——平方反比律——有心力（保守场）

• 电场强度矢量——高斯定理——通量——散度——有源场

• 电势——环路定理——环量——旋度——无旋场

• 场强与电势的关系——梯度

--- PAGE 025 ---
# 电容器的串联和并联

## 1. 电容器的串联

设各电荷带电量为 $q$

\[
V_1 = q/C_1, \quad V_2 = q/C_2, \quad \dots
\]

\[
V_{AB} = V_1 + V_2 + \dots + V_n = \left( \frac{1}{C_1} + \frac{1}{C_2} + \dots + \frac{1}{C_n} \right) q
\]

等效电容：

\[
\frac{1}{C} = \frac{1}{C_1} + \frac{1}{C_2} + \dots + \frac{1}{C_n}
\]

--- PAGE 025 ---
\[
\begin{align*}
\iiint \vec{D} \cdot d\vec{S} &= D_1 2\pi r^2 + D_2 2\pi r^2 = Q \\
(D_1 + D_2) 2\pi r^2 &= Q
\end{align*}
\]

\[
\begin{align*}
D_1 &= \varepsilon_0 E_1 = \varepsilon_0 E \quad ; \quad D_2 = \varepsilon_0 \varepsilon_r E_2 = \varepsilon_0 \varepsilon_r E \\
(1 + \varepsilon_r) \varepsilon_0 E \cdot 2\pi r^2 &= Q
\end{align*}
\]

\[
\begin{align*}
E &= \frac{Q}{2\pi(1 + \varepsilon_r)\varepsilon_0 r^2} \\
D_1 &= \varepsilon_0 E = \frac{Q}{2\pi(1 + \varepsilon_r)r^2} \\
D_2 &= \varepsilon_0 \varepsilon_r E = \frac{\varepsilon_r Q}{2\pi(1 + \varepsilon_r)r^2}
\end{align*}
\]

--- PAGE 026 ---
\[
E_x = \int dE_x = \int_{\theta_1}^{\theta_2} \frac{\lambda}{4\pi\varepsilon_0 a} \cos\theta d\theta
= \frac{\lambda}{4\pi\varepsilon_0 a} (\sin\theta_2 - \sin\theta_1)
\]

\[
E_y = \int dE_y = \int_{\theta_1}^{\theta_2} \frac{\lambda}{4\pi\varepsilon_0 a} \sin\theta d\theta
= \frac{\lambda}{4\pi\varepsilon_0 a} (\cos\theta_1 - \cos\theta_2)
\]

讨论

(1) \(a \gg L\) 杆可以看成点电荷

\[
E_x = 0, \quad E_y = \frac{\lambda L}{4\pi\varepsilon_0 a^2}
\]

(2) 无限长直导线

\[
\theta_1 = 0, \quad \theta_2 = \pi
\quad \Rightarrow \quad
\begin{cases}
E_x = 0 \\[4pt]
E_y = \dfrac{\lambda}{2\pi\varepsilon_0 a}
\end{cases}
\]

*(此处有插图)*

--- PAGE 026 ---
例. 均匀带电圆环，带电量为\(q\)，半径为\(a\)。求轴线上任一点\(P\)的场强。

解：

\[V = \frac{q}{4\pi\epsilon_0\sqrt{x^2 + a^2}}\]

\[E = E_x = -\frac{dV}{dx} = \frac{qx}{4\pi\epsilon_0(x^2 + a^2)^{3/2}}\]

--- PAGE 026 ---
## 2. 电容器的并联

\[
q_1 = C_1 V_{AB}, \quad q_2 = C_2 V_{AB}, \quad \dots
\]

总电量：

\[
q = q_1 + q_2 + \cdots + q_n = (C_1 + C_2 + \cdots + C_n) V
\]

等效电容：

\[
C = \frac{q}{V} = C_1 + C_2 + \cdots + C_n
\]

结论：并联电容器的等效电容等于各电容器电容之和。

--- PAGE 026 ---
\[
U = \int \vec{E} \cdot d\vec{l} = \int_{R_1}^{R_2} E \, dr
\]

\[
= \int_{R_1}^{R_2} \frac{Q}{2\pi\varepsilon_0 (1+\varepsilon_r)r^2} \, dr
\]

\[
= \frac{Q}{2\pi\varepsilon_0 (1+\varepsilon_r)} \left( \frac{1}{R_1} - \frac{1}{R_2} \right)
\]

\[
= \frac{Q}{2\pi\varepsilon_0(1+\varepsilon_r)} \frac{R_2 - R_1}{R_1 R_2}
\]

电容为

\[
C = \frac{Q}{U} = 2\pi\varepsilon_0 (1+\varepsilon_r) \frac{R_1 R_2}{R_2 - R_1}
\]

也可以把球形电容看成是两个半球电容的并联。

由球形电容器可知：

\[
C_1 = \frac{1}{2} \left( \frac{4\pi\varepsilon_0 R_1 R_2}{R_2 - R_1} \right)
\]

\[
C_2 = \frac{1}{2} \left( \frac{4\pi\varepsilon_0 \varepsilon_r R_1 R_2}{R_2 - R_1} \right)
\]

\[
C = C_1 + C_2 = 2\pi\varepsilon_0 (1 + \varepsilon_r) \frac{R_1 R_2}{R_2 - R_1}
\]

--- PAGE 027 ---
例 求电偶极子在均匀电场中受到的力偶矩。

解 \(F_+ = q\vec{E}\)，\(F_- = -q\vec{E}\)

相对于 0 点的力矩

\[
M = F_+ \cdot \frac{1}{2} l \sin\theta + F_- \cdot \frac{1}{2} l \sin\theta
= q l E \sin\theta
\]

\[
\vec{M} = q\vec{l} \times \vec{E} = \vec{p} \times \vec{E}
\]

讨论

(1) \(\theta = \frac{\pi}{2}\) 力偶矩最大
(2) \(\theta = 0\) 力偶矩为零（电偶极子处于稳定平衡）
(3) \(\theta = \pi\) 力偶矩为零（电偶极子处于非稳定平衡）

*(此处有插图)*

--- PAGE 027 ---
- **电容器的应用**：
  储能、振荡、滤波、移相、旁路、耦合等。

- **电容器的分类**：
  - 形状：平行板、柱形、球形电容器等
  - 介质：空气、陶瓷、涤纶、云母、电解电容器等
  - 用途：储能、振荡、滤波、移相、旁路、耦合电容器等

--- PAGE 027 ---
## 五、电介质中的电场能量与能量密度

➤ 介质中的电场能量密度

\[
W = \frac{1}{2} CU^2_{AB} = \frac{\varepsilon_0 \varepsilon_r S}{2d} E^2 d^2 = \frac{1}{2} EDV
\]

\[
W_e = \frac{1}{2} \varepsilon_0 \varepsilon_r E^2 = \frac{1}{2} DE
\]

这是电场能量密度的普遍表达式：

\[
W_e = \frac{1}{2} \vec{D} \cdot \mathbf{E}
\]

由此可以解决有电介质存在时静电场的能量问题。

--- PAGE 028 ---
### 一. 电场线（电力线）

- 起始于正电荷（或无穷远处），终止于负电荷（或无穷远处）。
- 场强方向沿电力线切线方向，场强大小决定电力线的疏密。

\[
E = \frac{dN}{dS_{\perp}}
\]

- 电场线是非闭合曲线，不相交。

*(此处有插图)*

--- PAGE 028 ---
# 9.8 电场能量

以平行板电容器为例，来计算电场能量。

设在时间 $t$ 内，从 $B$ 板向 $A$ 板迁移了电荷 $q(t)$

\[
u(t) = \frac{q(t)}{C}
\]

在将 $dq$ 从 $B$ 板迁移到 $A$ 板需作功

\[
dA = u(t) dq = \frac{q(t)}{C} dq
\]

极板上电量从 $0$ 到 $Q$ 作的总功为

\[
A = \int dA = \int_0^Q \frac{q(t)}{C} dq = \frac{Q^2}{2C}
\]

--- PAGE 028 ---
## 书中例题8.38(p.348)

平行板电容器的极板面积为 S，极板间距 d，中间充满相对介电常数为 $\varepsilon_r$ 的电介质。当充电后，两极板间的电势差为 $\Delta u$。

**求：**(1) 电容器中电场的能量

(2) 如果切断充电电源，把电介质从电容器中抽出来，外界要作多少功。

解：对于平行板介质电容器，其电容为：

\[
C = \varepsilon_r C_0 = \frac{\varepsilon_r \varepsilon_0 S}{d}
\]

电势差 $\Delta u = Ed$，电场的能量为：

\[
W = \frac{1}{2} C \Delta u^2 = \frac{1}{2} \frac{\varepsilon_r \varepsilon_0 S}{d} E^2 d^2 = \frac{1}{2} \varepsilon_r \varepsilon_0 E^2 S d = \frac{1}{2} \varepsilon E^2 V
\]

电场的能量密度为：

\[
w = \frac{W}{V} = \frac{1}{2} \varepsilon E^2 = \frac{1}{2} DE
\]

--- PAGE 029 ---
# 场的概念、标量场和矢量场 通量的概念

流体的速度——流速场

流速场的通量——流量

\[
\vec{v} \cos\theta dS = v_{\perp} dS
\]

*(此处有插图)*

--- PAGE 029 ---
\[
W = A = \frac{Q^2}{2C} \quad \xrightarrow{Q=CU} \quad = \frac{1}{2} CU^2 = \frac{1}{2} QU
\]

忽略边缘效应，对平行板电容器有

\[
U = Ed, \quad C = \frac{\varepsilon_0 S}{d}
\]

\[
W = \frac{1}{2} \varepsilon_0 E^2 S d = \frac{1}{2} \varepsilon_0 E^2 V
\]

能量密度 $w = \dfrac{W}{V} = \dfrac{1}{2} \varepsilon_0 E^2$ (适用于所有电场)

不均匀电场中 $dW = w \, dV$

\[
W = \int_V dW = \int_V \frac{1}{2} \varepsilon_0 E^2 dV
\]

--- PAGE 029 ---
充电后，极板所带的电量为：

\[
Q = C \Delta u = \frac{\varepsilon_r \varepsilon_0 S}{d} \Delta u
\]

切断电源，极板上的电量 Q 不变，抽出电介质后，电容器的电容变为：

\[
C_0 = \frac{\varepsilon_0 S}{d}
\]

此时电容器中电场的能量为：

\[
W' = \frac{Q^2}{2C_0} = \frac{\left(\frac{\varepsilon_r \varepsilon_0 S}{d} \Delta u\right)^2}{2 \frac{\varepsilon_0 S}{d}} = \frac{\varepsilon_r^2 \varepsilon_0 S}{2d} \Delta u^2
\]

--- PAGE 030 ---
## 环量的概念

流速场的环量——环流

流体的涡旋运动是围绕一条轴线（称为涡线）进行的，涡线或者通向流体的边界，或者在流体内形成闭合曲线。

\[
v \cdot dl = v \cos\theta dl = v_{\parallel} dl
\]

流速场沿着一个闭合环路的积分，表示沿着该环路流速分量的总和，称为环流。

通量和环量反映了矢量场在一定的连续有限空间内的分布规律和性质。

*(此处有插图)*

--- PAGE 030 ---
## 书中例题 8.33(P.338) 【重点】

半径为 $a$，带电量为 $q$ 的孤立金属球，求：它所产生的电场储存的静电能。

解：由高斯定理可求出电场强度

\[
E = \frac{1}{4\pi\varepsilon_0} \frac{q}{r^2}
\]

半径为 $r$，厚度为 $dr$ 的球壳中的静电能为：

\[
dW = w \, dV = \frac{1}{2} \varepsilon_0 E^2 \cdot 4\pi r^2 dr
\]

\[
= \frac{1}{2} \varepsilon_0 \left( \frac{1}{4\pi\varepsilon_0} \frac{q}{r^2} \right)^2 4\pi r^2 dr = \frac{q^2}{8\pi\varepsilon_0 r^2} dr
\]

整个空间中电场的能量为 $a$ 到 $\infty$ 的积分

\[
W = \int_V dW = \int_a^\infty \frac{q^2}{8\pi\varepsilon_0 r^2} dr = \frac{q^2}{8\pi\varepsilon_0 a}
\]

--- PAGE 030 ---
抽出电介质前后，电容器中电场能量之差等于外界所作的功：

\[
W' - W = \frac{\varepsilon_r^2 \varepsilon_0 S}{2d} \Delta u^2 - \frac{\varepsilon_r \varepsilon_0 S}{2d} \Delta u^2 = \frac{1}{2} \varepsilon_r \varepsilon_0 S \Delta u^2 \left( \frac{\varepsilon_r - 1}{d} \right)
\]

介质抽走以后，电场增强了，能量增加了，增加的部分来自于抽出介质时外力所作的功。

--- PAGE 031 ---
### 二. 电通量

在电场中穿过任意曲面 \(S\) 的电场线条数称为穿过该面的电通量 —— \(\Phi_e\)

定义 \(d\Phi_e = \vec{E} \cdot d\vec{S}\)

*(此处有插图)*

--- PAGE 031 ---
## 书中例题 8.33(P.338) 【重点】

圆柱形电容器长为 $L$，半径分别为 $R_1$、$R_2$，长度 $L \gg (R_2 - R_1)$，带电量分别为 $+Q$ 和 $-Q$。

求：球形电容器的电场中的能量。

解：由高斯定理可求出电场强度为：

\[
E = \frac{q}{2\pi\varepsilon_0 L r}
\]

电场能量密度为：

\[
w = \frac{1}{2} \varepsilon_0 E^2 = \frac{q^2}{8\pi^2 \varepsilon_0 L^2 r^2}
\]

--- PAGE 031 ---
# 书中例题8.39(p.349)(重点)

球形电容器中充满了相对介电常数为 $\varepsilon_r$ 的各向同性均匀介质。给电容充电，使其两极上带电量为 $\pm q$。

求：电容器中电场的能量。

解：由高斯定理求得：

\[
D = \frac{q}{4\pi r^2} \quad E = \frac{D}{\varepsilon_0 \varepsilon_r} = \frac{q}{4\pi \varepsilon_0 \varepsilon_r r^2}
\]

\[
dW = w \, dV = \frac{1}{2} DE \, dV
\]

\[
\frac{1}{2} \frac{q}{4\pi r^2} \cdot \frac{q}{4\pi \varepsilon_0 \varepsilon_r r^2} \cdot 4\pi r^2 dr = \frac{q^2}{8\pi \varepsilon_0 \varepsilon_r r^2} dr
\]

\[
W = \int_{R_1}^{R_2} dW = \int_{R_1}^{R_2} \frac{q^2}{8\pi \varepsilon_0 \varepsilon_r r^2} dr = \frac{q^2}{8\pi \varepsilon_0 \varepsilon_r} \left( \frac{1}{R_1} - \frac{1}{R_2} \right)
\]

--- PAGE 032 ---
1. 均匀场中

\[
\begin{aligned}
d\Phi_e &= \vec{E} \cdot d\vec{S} = E \cos\theta dS \\
&= E dS_{\bot}
\end{aligned}
\]

2. 非均匀场中

\[
d\Phi_e = \vec{E} \cdot d\vec{S}
\]

\[
\Phi_e = \int d\Phi_e = \int_S \vec{E} \cdot d\vec{S}
\]

对闭合曲面

\[
\Phi_e = \oint_S \vec{E} \cdot d\vec{S}
\]

*(此处有插图)*

--- PAGE 032 ---
取圆柱薄层半径为 $r$，厚度为 $dr$，长为 $L$，则体元为：

\[
dV = 2\pi r L dr
\]

体元中电场的能量：

\[
dW = w \, dV = \frac{q^2}{8\pi^2 \varepsilon_0 L^2 r^2} \cdot 2\pi r L dr = \frac{q^2}{4\pi \varepsilon_0 L r} dr
\]

圆桶之间的电场能量为 $R_1$ 到 $R_2$ 间的积分：

\[
W = \int_V w \, dV = \int_{R_1}^{R_2} \frac{q^2}{4\pi \varepsilon_0 L} \frac{dr}{r} = \frac{q^2}{4\pi \varepsilon_0 L} \ln \frac{R_2}{R_1}
\]

--- PAGE 032 ---
# 第六次作业

作业：8.33; 8.34; 8.35; 8.40; 8.41; 8.56; 8.58; 8.60

补充作业1：平行板电容器，极板 A 和 B 的面积为 S，两极板间距为 d，且 $d^2 \ll S$，联结电源后，A 板电势为 U，B 板电势为零。现将一带电量为 q，面积为 S 而厚度可忽略不计的导体片 C 平行地插在两极板的中间位置，如右图所示，求 C 片的电势 U。

补充作业2：一平行板电容器面积为 S，板间距为 d，两极室放着。若电容器两板充电到电压为 U 时，断开电源，使电容器的一半浸在相对介电常数为 $\varepsilon_r$ 的液体中，求浸入液体后：

(1) 电容器的静电能；(2) 极板上自由电荷面密度的分布。

--- PAGE 033 ---
讨论

(1) \(\vec{S}\) 方向的规定：
非闭合曲面 —— 凸为正，凹为负
闭合曲面 —— 向外为正，向内为负

(2) 电通量是代数量

\[
0 < \theta < \frac{\pi}{2} \rightarrow d\Phi_e \text{ 为正}
\]
\[
\frac{\pi}{2} < \theta < \pi \rightarrow d\Phi_e \text{ 为负}
\]

*(此处有插图)*

--- PAGE 033 ---
# 书中例题 8.35(P.339)

如图两电容并联

$C_1 = 1 \, \mu\text{F}$, $u_1 = 100 \, \text{V}$

$C_2 = 2 \, \mu\text{F}$, $u_2 = 200 \, \text{V}$

求：并联前后电容器所储存的静电能。

解：并联前

\[
W_1 = \frac{1}{2} C_1 u_1^2 = \frac{1}{2} \times 1.0 \times 10^{-6} \times 100^2 = 0.005 \, (\text{J})
\]

\[
W_2 = \frac{1}{2} C_2 u_2^2 = \frac{1}{2} \times 2.0 \times 10^{-6} \times 200^2 = 0.04 \, (\text{J})
\]

总能量：$W = W_1 + W_2 = 0.045 \, \text{J}$

并联后，$C = C_1 + C_2$，$Q = Q_1 + Q_2$

\[
W = \frac{Q^2}{2C} = \frac{(Q_1 + Q_2)^2}{2C} = \frac{(C_1 u_1 + C_2 u_2)^2}{2C} = 0.042 \, (\text{J})
\]

--- PAGE 034 ---
## 三. 高斯定理

\[
\Phi_e = \oint_S \vec{E} \cdot d\vec{S} = \frac{1}{\varepsilon_0} \sum_i q_i \ (\text{内})
\]

(不连续分布的源电荷)

\[
\Phi_e = \oint_S \vec{E} \cdot d\vec{S} = \frac{1}{\varepsilon_0} \int_V \rho dV
\]

(连续分布的源电荷)

真空中的任何静电场中，穿过任一闭合曲面的电通量，在数值上等于该面内包围的电量的代数和乘以 \(1/\varepsilon_0\)。定理中的任意闭合曲面称为"高斯面"。

\[
\Phi_e = \oint_S \vec{E} \cdot d\vec{S} \quad
\begin{cases}
> 0 \rightarrow +q \\
< 0 \rightarrow -q
\end{cases}
\]

*(此处有插图)*

--- PAGE 035 ---
# 高斯定理的证明

## (1) 点电荷 \(q\) 对任意封闭曲面的电通量

### 曲面上的面元 \(dS\) 的电通量为：

\[
d\Phi_e = \vec{E} \cdot d\vec{S} = \frac{q}{4\pi\varepsilon_0} \frac{\vec{e}_r \cdot d\vec{S}}{r^2}
\]

面元 \(dS\) 对 \(q\) 处所张立体角：

\[
d\Omega = \frac{dS_0}{r^2} = \frac{\vec{e}_r \cdot d\vec{S}}{r^2}
\]

因此，点电荷 \(q\) 对任意曲面的电通量为：

\[
\Phi_e = \oint_S \vec{E} \cdot d\vec{S} = \frac{q}{4\pi\varepsilon_0} \oint_S d\Omega
\]

积分的取值决定于点电荷位于面元的内部还是外部。

*(此处有插图)*

--- PAGE 036 ---
(2) 点电荷在曲面内部

点电荷在封闭曲面内部穿进穿出的次数总是奇数次，曲面对 \(q\) 点所张的立体角与单位球相同，为 \(4\pi\)

\[
\Phi_e = \oint_S \vec{E} \cdot d\vec{S} = \frac{q}{4\pi\varepsilon_0} \oint_S d\Omega
= \frac{q}{4\pi\varepsilon_0} \cdot 4\pi = \frac{q}{\varepsilon_0}
\]

*(此处有插图)*

--- PAGE 037 ---
任意封闭曲面对曲面内任意一点所张的立体角与单位球对球心所张立体角相同，均为 \(4\pi\)。

- 取球对称闭合曲面

\[
\Phi_e = \oint_S \vec{E} \cdot d\vec{S} = E \oint_S dS
= \frac{1}{4\pi\varepsilon_0} \frac{q}{r^2} \cdot 4\pi r^2 = \frac{1}{\varepsilon_0} q
\]

- 取任意闭合曲面时

\[
\Phi_e = \oint_S \vec{E} \cdot d\vec{S} = \frac{1}{\varepsilon_0} q
\]

结论：\(\Phi_e\) 与曲面的形状及 \(q\) 在曲面内的位置无关。

*(此处有插图)*

--- PAGE 038 ---
(3) 点电荷在曲面外部

\(q\) 在封闭曲面外，则曲面上的任意一面元 \(dS_1\) 对 \(q\) 张的立体角总与对应的另一面元 \(dS_2\) 对 \(q\) 张立体角大小相等，正负值相反。

因此，总通量为零。

--- PAGE 039 ---
- 当存在多个电荷时：

\[
\vec{E} = \vec{E}_1 + \vec{E}_2 + \cdots + \vec{E}_n
\]

\[
\Phi_e = \oint \vec{E} \cdot d\vec{S}
= \oint (\vec{E}_1 + \vec{E}_2 + \cdots + \vec{E}_n) \cdot d\vec{S}
= \oint \vec{E}_1 \cdot d\vec{S} + \oint \vec{E}_2 \cdot d\vec{S} + \cdots + \oint \vec{E}_n \cdot d\vec{S}
= \frac{q_1}{\varepsilon_0} + \frac{q_2}{\varepsilon_0} + \frac{q_3}{\varepsilon_0} + \cdots
\]

**结论：** \(\vec{E}\) 是所有电荷产生的，\(\Phi_e\) 只与内部电荷有关。

高斯面外的电荷对总通量没有贡献，对总场强有贡献。从高斯定理可以推导出电场线的性质。

*(此处有插图)*

--- PAGE 040 ---
# 高斯定理的物理意义

反映静电场的第一个基本性质——静电场是有源场

高斯定理积分形式：

\[
\oint_S \vec{E} \cdot d\vec{S} = \frac{1}{\varepsilon_0} \int_V \rho dV
\]

由 \(\oint_S \vec{E} \cdot d\vec{S} = \int_V \nabla \cdot \vec{E} \, dV = \frac{1}{\varepsilon_0} \int_V \rho dV\)

高斯定理微分形式：

\[
\nabla \cdot \vec{E} = \frac{\partial E_x}{\partial x} + \frac{\partial E_y}{\partial y} + \frac{\partial E_z}{\partial z} = \frac{\rho}{\varepsilon_0}
\]

它反映空间中某点电场的散度

- 散度 (divergence) 可用于表征空间各点矢量场发散的强弱程度，它是通量在空间点上的体密度，它是一个标量。物理上，散度的意义是场的有源性。通量描述了一定区域中场的方向趋势，散度则是这个性质的一种局部描述。当 \(\nabla \cdot \vec{F} > 0\)，表示该点有散发通量的正源（发散源）；当 \(\nabla \cdot \vec{F} < 0\) 表示该点有吸收通量的负源（汇）；当 \(\nabla \cdot \vec{F} = 0\)，表示该点无源。

--- PAGE 041 ---
高斯定理给出了场和场源的联系，它是场强对封闭曲面通量与场源的联系，而非场本身与源的联系。高斯定理指出电荷是静电场的源。

高斯定理与库仑定律的关系：高斯定理是由库仑定律导出的，但其适用范围却远超过库仑定律。但高斯定理不能反映静电场有心力场和平方反比率的特性。

高斯定理在电磁学中的重要地位和适用范围：高斯定理是描述电磁现象的四个基本方程之一。它适用于一切宏观电磁场，不仅适用于静电场，还适用于变化或运动的电场。

这章末尾将给出高斯定理的更普遍的形式。

--- PAGE 042 ---
## 四. 高斯定理的应用（所有例题均为重点）

**高斯定理应用之一：计算通过闭合曲面或部分曲面的电通量**

例如求通过如下正方体面的电通量：

封闭面的通量 \(\displaystyle \Phi = \frac{q}{\varepsilon_0}\)

每个面的通量 \(\displaystyle \Phi = \frac{q}{6\varepsilon_0}\)

所求曲面为不闭合曲面时，要考虑带电体对称性和电场分布对称性将该曲面补为闭合曲面才能应用高斯定理。

**思考题：** 闭合曲面 \(S\) 内有一点电荷 \(q\)，\(P\) 为 \(S\) 面上一点，在 \(S\) 面外 \(A\) 点有一点电荷 \(q'\)，若将 \(q'\) 移到 \(B\) 点，则（ ）

（A）穿过 \(S\) 面的电通量改变，\(P\) 点的电场强度不变
（B）穿过 \(S\) 面的电通量不变，\(P\) 点的电场强度改变
（C）穿过 \(S\) 面的电通量和 \(P\) 点的电场强度都不变
（D）穿过 \(S\) 面的电通量和 \(P\) 点的电场强度都改变

*(此处有插图)*

--- PAGE 043 ---
高斯定理的主要应用是求特殊对称分布带电体的场强。计算场强的条件：

带电体的电场强度分布要具有高度的对称性。

(1) 高斯面上的电场强度大小处处相等；
(2) 面积元 \(dS\) 的法线方向与该处的电场强度的方向一致。

因此，应用高斯定理求 \(E\) 除对电场分布有要求以外，关键是选取合适的高斯面。选取原则：

\[
\oint \vec{E} \cdot d\vec{S} = E \cdot S = \frac{\sum q}{\varepsilon_0}
\]

1. 高斯面必须经过所求场点
2. 在求 \(E\) 的部分高斯面上，要求该面上各点 \(E\) 的大小、方向处处相同（通常使 \(\vec{E} \parallel \vec{n}\)，或 \(\cos\theta = 1\)）。目的是可以把 \(E\) 从积分号内提出来。
3. 不求 \(E\) 的部分高斯面 \(\vec{E} \perp \vec{n}\)，使 \(\vec{E} \cdot d\vec{S} = 0\)
4. 按 1、2、3 要求所作的高斯面，要容易计算面积，通常选取柱面、球面等形状。

--- PAGE 044 ---
**例** 已知"无限长"均匀带电直线的电荷线密度为 \(+\lambda\)

**求** 距直线 \(r\) 处一点 \(P\) 的电场强度

**解** 电场分布具有轴对称性

过 \(P\) 点作一个以带电直线为轴，以 \(l\) 为高的圆柱形闭合曲面 \(S\) 作为高斯面

\[
\Phi_e = \oint_S \vec{E} \cdot d\vec{S}
= \oint_{侧} \vec{E} \cdot d\vec{S} + \oint_{上底} \vec{E} \cdot d\vec{S} + \oint_{下底} \vec{E} \cdot d\vec{S}
= \oint_{侧} E dS = E \oint_{侧} dS = E \cdot 2\pi r \cdot l
\]

*(此处有插图)*

--- PAGE 045 ---
根据高斯定理得

\[
\begin{aligned}
E \cdot 2\pi r \cdot l &= \frac{1}{\varepsilon_0} \lambda l \\[4pt]
E &= \frac{\lambda}{2\pi \varepsilon_0 r}
\end{aligned}
\]

电场分布曲线

*(此处有插图)*

--- PAGE 046 ---
**例** 均匀带电球面，总电量为 \(Q\)，半径为 \(R\)

**求** 电场强度分布

**解** 对球面外一点 \(P\)：

取过场点 \(P\) 的同心球面为高斯面

\[
\oint_S \vec{E} \cdot d\vec{S} = \oint_S E dS = E \iint_S dS = E \cdot 4\pi r^2
\]

根据高斯定理

\[
E \cdot 4\pi r^2 = \frac{\sum_i q_i}{\varepsilon_0}
\]

\[
r > R \quad \sum_i q_i = Q
\]

\[
E = \frac{Q}{4\pi\varepsilon_0 r^2}
\]

*(此处有插图)*

--- PAGE 047 ---
对球面内一点：

\[
E = 0
\]

*(此处有插图，含电场分布曲线)*

--- PAGE 048 ---
**例** 已知球体半径为 \(R\)，带电量为 \(q\)（电荷体密度为 \(\rho\)）

**求** 均匀带电球体的电场强度分布

球外 (\(r \ge R\))

\[
E = \frac{1}{4\pi\varepsilon_0} \frac{q}{r^2} \hat{r}^0 = \frac{\rho}{3\varepsilon_0} \frac{R^3}{r^2} \hat{r}^0
\]

球内 (\(r < R\))

\[
\oint_S \vec{E} \cdot d\vec{S} = E \cdot 4\pi r'^2 = \frac{1}{\varepsilon_0} \cdot \frac{4}{3} \pi r'^3 \rho = \frac{1}{\varepsilon_0} q'
\]

\[
E = \frac{\rho}{3\varepsilon_0} r
\]

*(此处有插图)*

--- PAGE 049 ---
# 书中例题8.11(p.304)

例已知"无限大"均匀带电平面上电荷面密度为σ

求 电场强度分布

解 电场强度分布具有面对称性

选取一个圆柱形高斯面

\[\Phi_e = \int_S \vec{E} \cdot d\vec{S}\]

\[= \int_{\text{侧}} \vec{E} \cdot d\vec{S} + \int_{\text{左底}} \vec{E} \cdot d\vec{S} + \int_{\text{右底}} \vec{E} \cdot d\vec{S}\]

\[= 0 + ES + ES = 2ES\]

根据高斯定理有

\[2ES = \frac{1}{\epsilon_0} \sigma S \quad E = \frac{\sigma}{2\epsilon_0}\]

--- PAGE 050 ---
例已知无限大板电荷体密度为\(\rho\)，厚度为\(d\)

求电场场强分布

解选取如图的圆柱面为高斯面

板外：\(2ES = \frac{\rho S d}{\varepsilon_{0}}\)

\(E_{\text{外}} = \frac{\rho d}{2\varepsilon_{0}}\)

板内：

\[2ES = \frac{\rho S \cdot 2x}{\varepsilon_{0}}\\ E_{\text{内}} = \frac{\rho x}{\varepsilon_{0}}\]

--- PAGE 051 ---
# 总结

用高斯定理求电场强度的步骤（P306）：

(1) 分析电荷对称性；

(2) 根据对称性取高斯面；

高斯面必须是闭合曲面

高斯面必须通过所求的点

高斯面的选取使通过该面的电通量易于计算

(3) 根据高斯定理求电场强度。

--- PAGE 052 ---
## 第五次作业

作业: 8.4, 8.5, 8.6, 8.7, 8.18, 8.20, 8.22, 8.23

补充作业习题: 一均匀带电的细棒被弯成如图所示的对称形状, 为两段直导线和一段圆弧, 试问θ为何值时, 圆心O点处的场强为零.
