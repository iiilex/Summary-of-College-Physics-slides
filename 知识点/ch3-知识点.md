# 第 3 章 功和能

## 一、知识点总结

### 3.1 功
- **恒力的功**：$A = Fs\cos\theta = \vec{F}\cdot\vec{S}$。
- **变力的功**：元功 $\mathrm{d}A = \vec{F}\cdot\mathrm{d}\vec{r}$；沿路径 $L$ 从 $a$ 到 $b$：$A = \displaystyle\int_{a(L)}^b \vec{F}\cdot\mathrm{d}\vec{r}$。
  - 直角坐标：$A = \displaystyle\int_{a(L)}^b (F_x\,\mathrm{d}x + F_y\,\mathrm{d}y + F_z\,\mathrm{d}z)$。
  - 自然坐标：$A = \displaystyle\int_{a(L)}^b F\cos\theta\,\mathrm{d}s$。
- **说明**：
  1. 功是标量，可正可负；
  2. 合力的功等于各分力功的代数和；
  3. 一般功与路径有关。
  - 解题第一步：写出 $\mathrm{d}A$，把 $\mathrm{d}A$ 写成"正在变化的那个变量"的函数。
- **功率**：
  - 平均功率 $\bar P = \dfrac{\Delta A}{\Delta t}$；
  - 瞬时功率 $P = \dfrac{\mathrm{d}A}{\mathrm{d}t} = \vec{F}\cdot\vec{v} = Fv\cos\theta$。

### 3.2 几种常见力的功
- **重力的功**（只与始末高度差有关）：$A_{重} = mg(z_1 - z_2)$，路径无关。
  - 书上例 3.2：长 $L$ 质量 $M$ 的柔绳，B 端被提到与 A 端同高时重力作功 $A = -\dfrac{1}{4}MgL$（利用提起的部分质心 $y/2$）。
- **弹性力的功**（胡克定律 $F = -kx$）：$A = \displaystyle\int_{x_1}^{x_2} -kx\,\mathrm{d}x = \dfrac{1}{2}kx_1^2 - \dfrac{1}{2}kx_2^2$。只与始末形变有关；变形减小作正功。
- **万有引力的功**：$A = \displaystyle\int_{r_1}^{r_2} -G\dfrac{mM}{r^2}\mathrm{d}r = GmM\left(\dfrac{1}{r_2} - \dfrac{1}{r_1}\right)$。移近时作正功，远离时作负功。
- **摩擦力的功**：方向始终与速度方向相反，$A = -\mu mgs$，与路径有关（非保守力）。

### 3.3 动能定理
- **质点动能定理**：$A = \dfrac{1}{2}mv_2^2 - \dfrac{1}{2}mv_1^2 = E_{k2} - E_{k1}$。
  - 功是过程量，动能是状态量。
  - 只适用于惯性系。
- **质点系动能定理**：$\sum A_i = \sum A_{i外} + \sum A_{i内} = \sum \dfrac{1}{2}m_iv_{i2}^2 - \sum \dfrac{1}{2}m_iv_{i1}^2$。
  - 内力的矢量和为零，但内力功的代数和不一定为零（如炸弹爆炸）。
  - 整链条类问题中各部分间内力功之和为零。

### 3.4 势能 机械能守恒定律
- **保守力**：力所作的功与路径无关，只取决于始末相对位置；$\displaystyle\oint_L \vec{f}\cdot\mathrm{d}\vec{r} = 0$。重力、万有引力、弹性力都是保守力；摩擦力是非保守力。
- **势能**：相对量，无绝对大小；零点任意。
  - 重力势能：$E_p = mgz$（零点取在 $z=0$ 平面）。
  - 弹性势能：$E_p = \dfrac{1}{2}kx^2$（零点取在弹簧原长）。
  - 万有引力势能：$E_p = -G\dfrac{mM}{r}$（零点取在 $r\to\infty$）。
  - 球内引力势能 $E_p = -GMm\dfrac{3R^2 - x^2}{2R^3}$。
- **保守力与势能关系**：
  - 功是势能增量的负值：$A = -(E_{p2} - E_{p1}) = -\Delta E_p$。
  - 保守力是势能的负梯度：$\vec{F} = -\nabla E_p$，$\nabla = \dfrac{\partial}{\partial x}\vec{i} + \dfrac{\partial}{\partial y}\vec{j} + \dfrac{\partial}{\partial z}\vec{k}$。
  - 二维判断保守力：$\dfrac{\partial F_x}{\partial y} = \dfrac{\partial F_y}{\partial x}$。
- **平衡稳定性**：
  - 稳定平衡 $\dfrac{\mathrm{d}^2 E_p}{\mathrm{d}x^2} > 0$；
  - 不稳定平衡 $\dfrac{\mathrm{d}^2 E_p}{\mathrm{d}x^2} < 0$；
  - 随遇平衡 $\dfrac{\mathrm{d}^2 E_p}{\mathrm{d}x^2} = 0$。
- **机械能守恒定律**：当 $A_{外} + A_{非内} = 0$ 时，$\Delta E = 0$，即 $E = E_k + E_p = $ 常数。
  - 是对系统而言、对整个过程而言。

### 3.5 能量守恒定律
- 能量不能消失也不能创造，只能从一种形式转换为另一种形式；封闭系统的总能量守恒。
- 功是能量交换或转换的一种度量；机械能守恒是普遍能量守恒定律的特例。

## 二、公式汇总

- 公式1：$A = \displaystyle\int_{a(L)}^b \vec{F}\cdot\mathrm{d}\vec{r} = \int (F_x\,\mathrm{d}x + F_y\,\mathrm{d}y + F_z\,\mathrm{d}z)$
  说明：变力沿路径的功（线积分），$\mathrm{d}\vec{r}$ 是位移元；直角坐标下三个分量的功的代数和。

- 公式2：$A = \displaystyle\int_{a(L)}^b F\cos\theta\,\mathrm{d}s$
  说明：自然坐标下的变力功表示，$F\cos\theta$ 是力沿切向方向的分量，$\mathrm{d}s$ 是弧长元。

- 公式3：$P = \vec{F}\cdot\vec{v} = Fv\cos\theta$
  说明：瞬时功率，$P$ 的单位为 W（瓦特），1 W = 1 J/s。

- 公式4：$A_{重} = mg(z_1 - z_2)$
  说明：重力做的功等于重力大小乘以始末位置的高度差；只与始末位置有关，路径无关。

- 公式5：$A_{弹} = \dfrac{1}{2}kx_1^2 - \dfrac{1}{2}kx_2^2$
  说明：弹性力做的功，$x_1,x_2$ 为弹簧形变量；变形减小时作正功。

- 公式6：$A_{引} = GmM\left(\dfrac{1}{r_2} - \dfrac{1}{r_1}\right)$
  说明：万有引力做的功，$r_1,r_2$ 为质点到引力中心的距离；引力为吸引力，远离作负功。

- 公式7：$A_{摩} = -\mu mgs$
  说明：滑动摩擦力做的功，$s$ 是路径长度（注意是路径不是位移），与路径有关。

- 公式8：$A = E_{k2} - E_{k1} = \dfrac{1}{2}mv_2^2 - \dfrac{1}{2}mv_1^2$
  说明：质点动能定理，合力在某一路程上对质点做的功等于质点始末状态动能的增量；功是过程量，动能是状态量。

- 公式9：$\displaystyle\oint_L \vec{f}\cdot\mathrm{d}\vec{r} = 0$
  说明：保守力沿任意闭合路径一周做的功为零；这是保守力等价判据。

- 公式10：$E_{p重} = mgz$
  说明：重力势能（取 $z=0$ 为零点），与水平位置 $x,y$ 无关；势能零点的选取是任意的。

- 公式11：$E_{p弹} = \dfrac{1}{2}kx^2$
  说明：弹性势能，零点取在弹簧原长（$x=0$）；$k$ 为劲度系数。

- 公式12：$E_{p引} = -G\dfrac{mM}{r}$
  说明：万有引力势能，零点取在 $r\to\infty$；负号表示束缚态。

- 公式13：$A_{保} = -(E_{p2} - E_{p1}) = -\Delta E_p$
  说明：保守力做的功等于势能增量的负值。

- 公式14：$\vec{F} = -\nabla E_p = -\left(\dfrac{\partial E_p}{\partial x}\vec{i} + \dfrac{\partial E_p}{\partial y}\vec{j} + \dfrac{\partial E_p}{\partial z}\vec{k}\right)$
  说明：保守力是势能梯度的负值；势能曲线上某点斜率的负值就是该点处的保守力。

- 公式15：$E_k + E_p = $ 常数（条件 $A_{外} + A_{非内} = 0$）
  说明：机械能守恒定律，机械能为动能与势能之和。
