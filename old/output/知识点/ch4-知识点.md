# 第 4 章 冲量和动量

## 一、知识点总结

### 4.1 质点动量定理
- **动量**：$\vec{P} = m\vec{v}$，矢量，方向与速度方向相同。
- **牛顿第二定律**的两种表述：
  - $\vec{F} = m\dfrac{\mathrm{d}\vec{v}}{\mathrm{d}t}$（仅在 $m$ 为常量时成立）；
  - $\vec{F} = \dfrac{\mathrm{d}(m\vec{v})}{\mathrm{d}t} = \dfrac{\mathrm{d}\vec{P}}{\mathrm{d}t}$（更具普遍性，$m$ 为变量时仍成立）。
  - 物理意义：**力是质点动量的变化率**。
- **冲量**：$\vec{I} = \displaystyle\int_{t_0}^{t_1} \vec{F}\,\mathrm{d}t$。
  - 冲量是过程量，与力的作用过程有关；
  - 冲量方向不一定与某瞬时 $\vec{F}$ 方向相同，而是由 $\vec{F}(t)$ 的时间积分决定（由动量增量方向决定）。
- **质点动量定理**：
  \[
    m\vec{v}_2 - m\vec{v}_1 = \int_{t_1}^{t_2}\vec{F}\,\mathrm{d}t = \vec{I},
    \quad \Delta\vec{P} = \vec{I}.
  \]
  - 物理意义：质点动量的变化依赖于作用力对时间的累积过程；
  - 矢量性：冲量方向与动量增量方向相同。
- **平均力**：当 $\vec{F}(t)$ 形式未知或不可解析表达时：
  \[
    \bar{\vec{F}} = \frac{\int_{t_0}^{t_1}\vec{F}(t)\,\mathrm{d}t}{t_1 - t_0},\quad \vec{I} = \bar{\vec{F}}(t_1 - t_0).
  \]
  - 数学上利用了积分中值定理。
- **分量形式**：
  \[
    mv_{2x} - mv_{1x} = \int F_x\,\mathrm{d}t,\quad
    mv_{2y} - mv_{1y} = \int F_y\,\mathrm{d}t,\quad
    mv_{2z} - mv_{1z} = \int F_z\,\mathrm{d}t.
  \]
  - 冲量的任一分量等于在它自己方向上的动量分量的增量。

### 4.2 质点系动量定理
- **质点系的总动量**：$\vec{P} = \sum_i m_i\vec{v}_i$。
- **内力性质**：一对内力 $\vec{f}_{ij} + \vec{f}_{ji} = 0$（成对出现、大小相等方向相反）。
- **质点系动量定理**：
  \[
    \mathrm{d}\biggl(\sum_i m_i\vec{v}_i\biggr) = \sum_i \vec{F}_i\,\mathrm{d}t,
  \]
  \[
    \sum_i m_i\vec{v}_i - \sum_i m_i\vec{v}_{i0} = \sum_i \int_{t_0}^{t}\vec{F}_i\,\mathrm{d}t.
  \]
  - 只有外力可改变系统总动量，内力不改变系统总动量；
  - 内力可改变系统内单个质点的动量。
- **例**：子弹穿过两木块（质点系发生变化）。
  - 子弹穿过第一木块：$F\Delta t_1 = (m_1 + m_2)v_1 - 0 \Rightarrow v_1 = \dfrac{F\Delta t_1}{m_1 + m_2}$；
  - 子弹穿过第二木块：$F\Delta t_2 = m_2 v_2 - m_2 v_1 \Rightarrow v_2 = \dfrac{F\Delta t_1}{m_1 + m_2} + \dfrac{F\Delta t_2}{m_2}$。
- **例**：匀质链条 $M, L$ 上端悬挂下端落秤盘。任意时刻 $t$ 秤的读数 $N = mg + F = \dfrac{3M}{L}gx$（称盘上链条质量的 3 倍）。

### 4.3 质点系动量守恒定律
- **定律内容**：当 $\sum_i \vec{F}_i = 0$ 时，$\dfrac{\mathrm{d}}{\mathrm{d}t}\biggl(\sum m_i\vec{v}_i\biggr) = 0$，即 $\sum m_i\vec{v}_i = $ 常矢量。
- **分量形式**：
  \[
    F_x = 0 \Rightarrow \sum m_i v_{ix} = P_x = \text{常量},
  \]
  其它方向类似。
- **说明**：
  1. 动量守恒定律独立于牛顿定律，适用于高速和微观领域；
  2. 与空间平移不变性相联系（与时间平移不变性对应的能量守恒相并列）；
  3. **内力不改变系统总动量，但可改变系统内单个质点的动量**（如炸弹爆炸、人船问题、火箭喷气）。
- **应用要点**：
  - 系统观点：把涉及质点系看作一个整体；
  - 受力分析：合外力是否为零或某方向为零；
  - 统一惯性参考系：动量必须对同一惯性系写出，注意伽利略变换。
- **例**：长 $L$、质量 $M$ 船静止湖面，人质量 $m$ 从船头走到船尾。水平方向动量守恒 $\Rightarrow MS = ms$，结合 $S + s = L$，得 $S = \dfrac{m}{M+m}L$，$s = L - S$。
- **例**：木块 $m$ 沿斜面下滑，斜面 $M$ 自由滑动。水平方向动量守恒 $mv_x - MV = 0$ + 机械能守恒联立可解。
- **碰撞问题**（动量总是守恒）：
  - **完全弹性碰撞**：动量 + 动能都守恒，
    \[
      v_1 = \frac{(m_1 - m_2)v_{10} + 2m_2 v_{20}}{m_1 + m_2},\quad
      v_2 = \frac{(m_2 - m_1)v_{20} + 2m_1 v_{10}}{m_1 + m_2}.
    \]
  - **完全非弹性碰撞**：碰后共同速度 $v = \dfrac{m_1 v_{10} + m_2 v_{20}}{m_1 + m_2}$，动能有损失。
  - **非完全弹性碰撞**：引入恢复系数 $e = \dfrac{v_2 - v_1}{v_{10} - v_{20}}$（$0 \le e \le 1$），结合动量守恒求解。
- **变质量系统的统一公式**（密歇尔斯基方程）：
  \[
    F + v_r\frac{\mathrm{d}m}{\mathrm{d}t} = m\frac{\mathrm{d}v}{\mathrm{d}t},\quad
    \text{或}\quad F = m\frac{\mathrm{d}v}{\mathrm{d}t} - u\frac{\mathrm{d}m}{\mathrm{d}t}.
  \]
  - $u$ 为相对系统的质量流速度（$\mathrm{d}m$ 相对 $m$ 的速度）；
  - **火箭** $u \ne 0$：$m\,\mathrm{d}v = -u\,\mathrm{d}m$，积分得 **齐奥尔科夫斯基公式** $v = u\ln\dfrac{M_0}{M}$；
  - **漏沙车** $u = 0$：$F = m\dfrac{\mathrm{d}v}{\mathrm{d}t}$，回到牛顿第二定律（气体没带走额外动量）。

### 4.4 质心与质心运动定理
- **质心定义**（带权平均）：
  - 质点系：$\vec{r}_C = \dfrac{\sum m_i \vec{r}_i}{\sum m_i}$；
  - 连续体：$\vec{r}_C = \dfrac{\int \rho\,\vec{r}\,\mathrm{d}V}{\int \rho\,\mathrm{d}V}$；
  - 质心坐标（或位矢）与坐标原点的选取有关，但质心与体系各质点的相对位置与坐标原点选取无关。
- **质心运动定理**：
  \[
    \vec{F}_{ex} = \frac{\mathrm{d}\vec{P}}{\mathrm{d}t} = m_C\frac{\mathrm{d}^2\vec{r}_C}{\mathrm{d}t^2} = m_C\vec{a}_C.
  \]
- **质心动量定理**：$\displaystyle\int_{t_0}^t \vec{F}_{ex}\,\mathrm{d}t = m_C\vec{v}_C - m_C\vec{v}_{C0}$。
- **说明**：
  - 质心相当于将系统总质量集中于该点、所有外力等效作用于该点；
  - **内力对质心运动不产生任何影响**，不能产生质心加速度；
  - 系统动量守恒 $\Leftrightarrow$ 质心运动状态不变；
  - 地球上小物体，质心与重心重合；在太空仅质心有意义，重力不均匀时（如大山）质心与重心不重合。
- **质心坐标系**（质心系）：原点取在质心、轴方向与惯性系平行的平动坐标系。
  - 孤立体系或合外力为零的体系：质心系是惯性系；
  - 受外力作用的体系：质心系是非惯性系。

## 二、公式汇总

- 公式1：$\vec{P} = m\vec{v}$
  说明：动量定义；矢量，方向与速度方向相同；比 $m\vec{a}$ 更具普遍性（$m$ 变化时仍可描述）。

- 公式2：$\vec{F} = \dfrac{\mathrm{d}\vec{P}}{\mathrm{d}t}$
  说明：牛顿第二定律的更本质写法；说明力是动量的变化率，适用于 $m$ 变化的情况。

- 公式3：$\vec{I} = \displaystyle\int_{t_0}^{t_1}\vec{F}\,\mathrm{d}t$
  说明：冲量定义；过程量；方向由 $\vec{F}(t)$ 对时间的积分决定，不一定与瞬时 $\vec{F}$ 方向相同。

- 公式4：$m\vec{v}_2 - m\vec{v}_1 = \displaystyle\int_{t_1}^{t_2}\vec{F}\,\mathrm{d}t = \vec{I}$
  说明：质点动量定理；合力在某段时间内的冲量等于质点始末动量的矢量增量；只适用惯性系。

- 公式5：$\bar{\vec{F}} = \dfrac{1}{t_1 - t_0}\displaystyle\int_{t_0}^{t_1}\vec{F}(t)\,\mathrm{d}t$
  说明：平均力定义；$\vec{I} = \bar{\vec{F}}(t_1 - t_0)$；用于 $F(t)$ 形式未知或不能解析表达的情形；数学上由积分中值定理得到。

- 公式6：$\mathrm{d}\biggl(\sum_i m_i\vec{v}_i\biggr) = \sum_i \vec{F}_i\,\mathrm{d}t$
  说明：质点系动量定理（微分形式）；右边是外力之和（内力成对抵消）；只有外力可改变系统总动量。

- 公式7：$\sum_i m_i\vec{v}_i - \sum_i m_i\vec{v}_{i0} = \sum_i \displaystyle\int_{t_0}^{t}\vec{F}_i\,\mathrm{d}t$
  说明：质点系动量定理（积分形式）；某段时间内系统动量的增量等于外力冲量的矢量和。

- 公式8：$\sum_i \vec{F}_i = 0 \Rightarrow \sum_i m_i\vec{v}_i = $ 常矢量
  说明：质点系动量守恒定律；适用条件是合外力为零；守恒是矢量守恒，常给出分量方程。

- 公式9：$F = \dfrac{\mathrm{d}(m\vec{v})}{\mathrm{d}t}$ 或 $F + v_r\dfrac{\mathrm{d}m}{\mathrm{d}t} = m\dfrac{\mathrm{d}v}{\mathrm{d}t}$
  说明：变质量系统的统一公式（密歇尔斯基方程）；$v_r$ 为 $\mathrm{d}m$ 相对 $m$ 的速度；火箭问题 $v_r \ne 0$，漏沙问题 $v_r = 0$。

- 公式10：$v = u\ln\dfrac{M_0}{M}$
  说明：齐奥尔科夫斯基公式；不计外力时火箭最终速度；取决于喷气速度 $u$ 与质量比 $M_0/M$。

- 公式11：$\vec{r}_C = \dfrac{\sum_i m_i \vec{r}_i}{\sum_i m_i}$；连续体 $\vec{r}_C = \dfrac{\int \rho\,\vec{r}\,\mathrm{d}V}{\int \rho\,\mathrm{d}V}$
  说明：质心位矢定义；是带权平均（权为质量）；质心相对系统内各点的位置与坐标原点选取无关。

- 公式12：$\vec{F}_{ex} = m_C\vec{a}_C = m_C\dfrac{\mathrm{d}^2\vec{r}_C}{\mathrm{d}t^2}$
  说明：质心运动定理；合外力等于总质量乘以质心加速度；内力对质心运动无影响。

- 公式13：$\displaystyle\int_{t_0}^t \vec{F}_{ex}\,\mathrm{d}t = m_C\vec{v}_C - m_C\vec{v}_{C0}$
  说明：质心动量定理（积分形式）；外力冲量等于质心动量增量。

- 公式14：$v = \dfrac{m_1 v_{10} + m_2 v_{20}}{m_1 + m_2}$（完全非弹性碰撞）
  说明：碰后共同速度；动能不守恒，部分动能转化为内能。

- 公式15：$\begin{cases} v_1 = \dfrac{(m_1 - m_2)v_{10} + 2m_2 v_{20}}{m_1 + m_2} \\[4pt] v_2 = \dfrac{(m_2 - m_1)v_{20} + 2m_1 v_{10}}{m_1 + m_2} \end{cases}$（完全弹性碰撞）
  说明：动量、动能都守恒，联立求解；$m_1 = m_2$ 时两球交换速度；$m_2 \to \infty$ 时 $v_1 \approx -v_{10}$。
