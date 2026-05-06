# 🚗 Car Dataset Analysis Presentation

---

## Slide 1: Title & Overview

### 🚗 Car Dataset Analysis Report
**Complete Data Analysis & Machine Learning Pipeline**

---

### 📊 Dataset Overview
- **11,914** raw records → **11,090** after filtering
- **16** original columns → **18** with engineered features
- **Year Range:** 1995–2017
- **Analysis Scope:** Data cleaning, feature engineering, EDA, correlation analysis

---

## Slide 2: Data Cleaning - Missing Value Treatment

### 🔧 Missing Value Strategies

| Column | Missing | Strategy | Rationale |
|--------|---------|----------|-----------|
| Engine HP | 69 | Median per Make | Skewed distribution; preserves brand power profiles |
| Engine Cylinders | 30 | Median per Make | Integer ordinal; brand groups share configurations |
| Engine Fuel Type | 3 | Global mode | Only 3 missing; overwhelming majority gasoline |
| Number of Doors | 6 | Mode per Vehicle Style | Style dictates door count (coupes→2, sedans→4) |
| Market Category | 3,742 | Fill "Unknown" | ~31% missing; preserves rows, flagged as unknown |

---

## Slide 3: Data Cleaning - Processing Steps

### 🔄 Data Type Conversion & Filtering

#### Type Conversions
- **Engine Cylinders:** float64 → int (whole numbers after imputation)
- **Number of Doors:** float64 → int (discrete values)
- **Engine HP:** float64 kept (preserves decimal precision)

#### Year Filter
- **Criteria:** Year ≥ 1995
- **Removed:** 824 pre-1995 vehicles
- **Final Dataset:** 11,090 records

#### String Standardization
- Converted to lowercase to prevent duplicate keys
- Applied to: Vehicle Style, Market Category
- Example: "Sedan", "sedan", "SEDAN" → "sedan"

---

## Slide 4: Feature Engineering

### ⚙️ New Features Created

#### 📈 Total MPG
**Formula:** `(city mpg + highway MPG) / 2`
- **Purpose:** Single efficiency metric per vehicle
- **Statistics:**
  - Mean: **23.4**
  - Median: **22.0**
  - Max: **189.0**

#### 💰 Price per HP
**Formula:** `MSRP / Engine HP`
- **Purpose:** Cost-efficiency of horsepower
- **Statistics:**
  - Mean: **$150**
  - Median: **$138**
  - Max: **$2,308**

---

## Slide 5: Descriptive Statistics

### 📊 Key Dataset Metrics

| Metric | Engine HP | MSRP ($) | Popularity | Highway MPG | City MPG |
|--------|-----------|----------|------------|-------------|----------|
| **Mean** | 256.8 | $43,428 | 1,568 | 26.5 | 19.5 |
| **Median** | 240.0 | $31,250 | 1,385 | 26.0 | 18.0 |
| **Std Dev** | 108.8 | $61,533 | 1,452 | 7.5 | 6.6 |

### 💡 Key Insight
**MSRP Distribution:** Very high standard deviation ($61K on $43K mean) indicates heavily right-skewed distribution driven by ultra-luxury vehicles. Median ($31K) is more representative.

---

## Slide 6: Group Analysis - Drivetrain & Size

### 🚗 Analysis by Vehicle Characteristics

#### By Driven Wheels
| Type | Avg MSRP | Avg Popularity |
|------|----------|----------------|
| All Wheel Drive | $59,397 | 1,510 |
| Four Wheel Drive | $38,461 | 1,760 |
| Front Wheel Drive | $24,648 | 1,397 |
| Rear Wheel Drive | $60,469 | 1,776 |

**Insight:** RWD and AWD command highest prices; FWD most affordable.

#### By Vehicle Size
| Size | Avg MSRP | Avg Popularity |
|------|----------|----------------|
| Large | $56,787 | 1,906 |
| Midsize | $40,887 | 1,452 |
| Compact | $37,774 | 1,475 |

**Insight:** Large vehicles most expensive and popular (luxury SUVs/trucks).

---

## Slide 7: Group Analysis - Engine Performance

### ⚡ Engine Cylinders Impact

| Cylinders | Avg MSRP | Avg Popularity |
|-----------|----------|----------------|
| 0 (Electric) | $34,512 | 1,987 |
| 3 | $13,547 | 792 |
| 4 | $25,548 | 1,436 |
| 5 | $22,858 | 856 |
| 6 | $36,491 | 1,693 |
| 8 | $65,560 | 1,756 |
| 10 | $184,124 | 1,830 |
| 12 | $290,142 | 830 |
| 16 | $1,757,224 | 820 |

### 💡 Key Finding
**Strong positive relationship** between cylinder count and price. 16-cylinder vehicles (Bugatti Veyron-class) are extreme outliers.

---

## Slide 8: Visualizations - Distribution & Relationships

### 📈 Key Visualizations

#### City MPG Histogram
- **Distribution:** Right-skewed
- **Peak:** 15-25 MPG range
- **Tail:** Hybrids/electrics extending to 100+ MPG

#### Engine HP vs MSRP Scatter
- **Trend:** Clear positive correlation
- **Pattern:** Higher HP → Higher prices
- **Variation:** Wide spread at high HP (brand prestige effect)

#### MSRP by Driven Wheels Boxplot
- **Highest:** RWD and AWD
- **Lowest:** FWD
- **Variation:** Wider IQR for RWD/AWD (diverse luxury offerings)

#### MSRP by Vehicle Size Boxplot
- **Premium:** Large vehicles ~51% over Compact
- **Driver:** Luxury SUVs and full-size trucks

---

## Slide 9: Correlation Analysis

### 🔗 Variable Relationships

| Variable Pair | Correlation | Strength | Interpretation |
|---------------|-------------|----------|----------------|
| city mpg ↔ highway MPG | **+0.887** | **Strong ✓** | Same underlying fuel efficiency |
| Engine HP ↔ MSRP | **+0.661** | **Moderate–Strong ✓** | More power = higher price |
| Engine HP ↔ city mpg | **-0.354** | **Moderate ↓** | Performance vs economy trade-off |
| Engine HP ↔ highway MPG | **-0.360** | **Moderate ↓** | Same trade-off on highways |
| MSRP ↔ city mpg | **-0.158** | **Weak ↓** | Expensive cars slightly less efficient |
| Popularity ↔ any variable | **≈ 0.00** | **None** | Reflects brand/marketing, not specs |

### 💡 Key Insights
- **Strongest correlation:** City & Highway MPG (expected)
- **Most significant predictor:** Engine HP for MSRP
- **Independent factor:** Popularity uncorrelated with vehicle specs

---

## Slide 10: Summary & Conclusions

### 🎯 Key Takeaways

#### Data Quality
- Successfully cleaned 11,090 records from 11,914 raw
- Handled missing values with context-appropriate strategies
- Created meaningful engineered features

#### Market Insights
- **Premium segments:** RWD/AWD, Large vehicles, High-cylinder engines
- **Price drivers:** Engine HP (strong correlation), Vehicle size, Drivetrain
- **Efficiency trade-off:** Higher horsepower generally means lower MPG

#### Surprising Findings
- Popularity independent of technical specifications
- Extreme outliers in luxury segment (16-cylinder vehicles)
- Weak negative correlation between price and fuel efficiency

### 📈 Business Implications
- **Pricing strategy:** Focus on HP and vehicle positioning
- **Market segmentation:** Clear luxury vs mainstream divides
- **Efficiency marketing:** Hybrid/electric tail represents niche opportunity

---

## Slide 11: Technical Appendix

### 🛠️ Analysis Pipeline

#### Data Processing
1. **Missing value imputation** using domain knowledge
2. **Type conversion** for data integrity
3. **Feature engineering** for business insights
4. **Statistical analysis** for pattern discovery

#### Methodology
- **Correlation analysis** for variable relationships
- **Group analysis** for market segmentation
- **Visualization** for pattern discovery
- **Statistical validation** for insights

#### Tools & Techniques
- **Python pandas** for data manipulation
- **Statistical analysis** for insights
- **Data visualization** for communication
- **Feature engineering** for enhanced analysis

---

### 📊 Generated Files
- `car_analysis_report.html` - Full technical report
- `city_mpg_histogram.png` - Distribution analysis
- `engine_hp_vs_msrp.png` - Price-power relationship
- `msrp_by_driven_wheels.png` - Drivetrain analysis
- `msrp_by_vehicle_size.png` - Size segmentation
- `correlation_heatmap.png` - Variable relationships

---

**End of Presentation**
