DDL 用于定义和管理数据库结构（表、视图、索引等）。

1. **创建数据库**
   
    ```
    CREATE DATABASE DatabaseName;
    ```
    
2. **删除数据库**
   
    ```
    DROP DATABASE DatabaseName;
    ```
    
3. **创建表**
   
    ```sql
    CREATE TABLE DatabaseName.TableName (
        Column1 DataType Constraints,
        Column2 DataType Constraints,
        ...
    		PRIMARY KEY (<AttributeName>)
    		FOREIGN KEY (<AttributeName>) REFERENCES <TableName>(<ColumnName>) ON DELETE CASCADE
    );
    ```
    
4. **删除表**
   
    ```
    DROP TABLE TableName;
    ```
    
5. **修改表结构**
    - **添加列**
      
        ```
        ALTER TABLE TableName ADD ColumnName DataType;
        ```
        
    - **修改列数据类型**
      
        ```
        ALTER TABLE TableName MODIFY ColumnName NewDataType;
        ```
        
    - **删除列**
      
        ```
        ALTER TABLE TableName DROP COLUMN ColumnName;
        ```
        

---

DML 用于对数据库表中的数据进行增删改查。

1. **插入数据**
   
    ```
    INSERT INTO TableName (Column1, Column2, ...)
    VALUES (Value1, Value2, ...);
    ```
    
2. **更新数据**
   
    ```sql
    UPDATE TableName
    SET Column1 = Value1, Column2 = Value2
    WHERE Condition;
    ```
    
3. **删除数据**
   
    ```
    DELETE FROM TableName
    WHERE Condition;
    ```
    

---

DQL 是用于查询数据的 SQL 语句，`SELECT` 是最常用的 DQL 语句。

1. **基本查询**
   
    ```
    SELECT Column1, Column2
    FROM TableName;
    ```
    
2. **条件查询**
   
    ```
    SELECT Column1, Column2
    FROM TableName
    WHERE Condition;
    ```
    
3. **排序查询**
   
    ```
    SELECT Column1, Column2
    FROM TableName
    ORDER BY Column1 [ASC|DESC];
    ```
    
4. **分组查询**
   
    ```
    SELECT Column1, COUNT(*)
    FROM TableName
    GROUP BY Column1;
    ```
    
5. **聚合函数**
    - **计数**：`COUNT`
    - **平均值**：`AVG`
    - **最大值**：`MAX`
    - **最小值**：`MIN`
    - **总和**：`SUM`
    
    ```
    SELECT COUNT(*), AVG(ColumnName), MAX(ColumnName)
    FROM TableName;
    ```
    
6. **连接查询（JOIN）**
    - **内连接**
      
        ```
        SELECT a.Column1, b.Column2
        FROM TableA a
        JOIN TableB b ON a.CommonColumn = b.CommonColumn;
        ```
        
    - **左连接**
      
        ```
        SELECT a.Column1, b.Column2
        FROM TableA a
        LEFT JOIN TableB b ON a.CommonColumn = b.CommonColumn;
        ```
        
    - **右连接**
      
        ```
        SELECT a.Column1, b.Column2
        FROM TableA a
        RIGHT JOIN TableB b ON a.CommonColumn = b.CommonColumn;
        ```
    
7. **子查询**
   
    ```
    SELECT Column1
    FROM TableName
    WHERE Column2 = (SELECT MAX(Column2) FROM TableName);
    ```
    
8. **UNION 操作**
   
    ```
    SELECT Column1, Column2 FROM TableA
    UNION
    SELECT Column1, Column2 FROM TableB;
    ```
    
    使用 `UNION ALL` 可以保留重复行。
    

---

**视图（VIEW）**

1. **创建视图**
   
    ```
    CREATE VIEW ViewName AS
    SELECT Column1, Column2
    FROM TableName
    WHERE Condition;
    SHOW CREATE VIEW ViewName;//显示刚刚创建的视图的详细信息
    ```
    
2. **查询视图**
   
    ```
    SELECT * FROM ViewName;
    ```
    
3. **删除视图**
   
    ```
    DROP VIEW ViewName;
    ```
    

---

**索引（INDEX）**

1. **创建索引**
   
    ```
    CREATE INDEX IndexName ON TableName (ColumnName);
    ```
    
2. **删除索引**
   
    ```
    DROP INDEX IndexName ON TableName;
    ```
    

---

MySQL Data Types

- **VARCHAR(X)**: Variable-length character string of up to `X` characters.
- **CHAR(X)**: Fixed-length string of exactly `X` characters.
- **BOOLEAN**: Stores `TRUE` or `FALSE` values.
- **INT**: Integer type for whole numbers.
- **FLOAT**: Floating-point type for decimal numbers.
- DATE

---

Attribute Modifiers

- **AUTO_INCREMENT**: Automatically increments an integer field with each new row.
- **NOT NULL**: Ensures each row has a value in this field.

---

Modifying a Table

- **Add a Column**: `ALTER TABLE <TableName> ADD COLUMN ColumnName VARCHAR(255);`
- **Remove a Column**: `ALTER TABLE <TableName> DROP COLUMN <ColumnName>;`

---

Modifying (Altering a Field)

- **Rename a Column**: `ALTER TABLE <TableName> RENAME <OldColumnName> TO <NewColumnName>;`
- **Change Column Attributes**: `ALTER TABLE <TableName> MODIFY <ColumnName> <Modifiers>;`
  
    这部分可以包含新的数据类型、约束、默认值等修饰符。具体的修饰符取决于你想要进行的更改，如VARCHAR(100)。
    

Viewing (Reading) a Table Structure

- **Show Columns**（data types and attribute (field/column) names ）: `SHOW COLUMNS FROM <TableName>;`

---

Generated Columns

- **Creating a Generated Column**:创建一个计算列
  
    ```
    <ColumnName> GENERATED ALWAYS AS (<function>)
    ```
    

---

Additional Modifiers / Constraints

- **DEFAULT <defaultValue>**: Sets a default value for a field.
- **CHECK (<formula>)**: Ensures the field meets the specified constraint.用于确保列中的数据符合特定的条件或规则

---

Complex ‘WHERE’ Operators

- `=`: Equal to
- `<>` or `!=`: Not equal to
- `>` and `<`: Greater than, less than
- `LIKE`: Pattern matching
- `IN`: Matches any value from a list
- `BETWEEN`: Specifies a range

---

Complex ‘WHERE’ Keywords

- **AND**: Both sides must be true.
- **OR**: Either side must be true.
- **NOT**: Reverses the condition.

---

Comment Formats in Queries

- **#**: Single-line comment
- **-**: Another single-line comment style
- **/* ... */**: Multi-line comment

---

Show Create Table Command

- **Command**: `SHOW CREATE TABLE <TableName>;`

---

Aggregating Functions

- **Common Functions**:
    - `AVG()`, `MIN()`, `MAX()`, `SUM()`, `COUNT()`

---

Date Functions

- **MONTH(<ColumnName>)**: Groups by month.
- **YEAR(<ColumnName>)**: Groups by year.
- NOW()

Pivot Tables 透视表、view 视图、corrplot（相关图）

BI software: aims to simplify the process of putting together scattered分散 and disconnected断开 data sources and assist in the design of repositories资源库 and (visual, graphical) reports

report - a view of single dataset

dashboard - Composite views containing multiple reports.

App - a collection of report/ dashboard

transforming data

Operations like deriving new attributes, reshaping data, or adjusting data types

cleaning data

Dummy Vars哑变量：在数据分析中用于将分类变量（例如性别、国家、喜好等）转换成数值形式，以便在分析或建模时使用

binary variables二元变量 is not particularly statistically worthwhile. In other words, it will be either 1 or 0 – not much variability

Imported vs Connected Data: local or online

DAX language 

 R used for data analysis and visualisation

R 语言中，`corrplot` 函数用于绘制相关矩阵（correlation matrix），用来展示不同变量之间的相关关系

`corr_matrix <- cor(dataset)`:计算数据集中所有数值变量之间的相关性矩阵,将计算得到的相关性矩阵存储在变量 `corr_matrix` 中

`corrplot(corr_matrix)` :使用 `corrplot` 包中的 `corrplot` 函数绘制相关性图

**Correlation Plot**（相关性图）是一种用于可视化变量之间相关性的工具。它通过图形化方式展示多个变量之间的相关性，以帮助识别变量之间的关系和模式。这种图通常使用颜色编码来表示相关性强度和方向。

```r
# 绘制相关性图
corrplot(corr_matrix, method = "circle", type = "upper", 
         tl.col = "black", tl.srt = 45, # 标签颜色和旋转
         addCoef.col = "black", # 添加相关系数值
         diag = FALSE) # 不显示对角线
# method = "circle": 使用圆形表示相关性强度。可选择其他方法，如 "square" 或 "number"。
# type = "upper": 仅显示相关性矩阵的上三角部分。
```

spatial data（空间数据）指的是包含地理位置信息的数据

矢量数据（Vector Data）：Point坐标，Polygon面积，Line道路

栅格数据（Raster Data）：使用像素（网格单元）来表示空间上的连续变化，通常用于遥感图像或地形图。

创建空间数据类型 CREATE TABLE GeometryTable (geometry POINT);

插入数据时，使用经纬度 ST_GeomFromText(‘POINT(<Long> <Lat>)’)

Spatial Queries

`SELECT * FROM <TableName> WHERE ST_Distance_Sphere(<GeomField>,
ST_GeomFromText(<Location>)) <= 10 * 1000 ORDER BY name;`

the bubble map VS a filled (choropleth等值线) map

- **气泡地图**：在一个国家或地区的中心显示气泡大小，但可能会遮挡地图细节。
- **填充地图**：地图的每个区域根据数据值被赋予不同的颜色深度，使数据的地理分布一目了然，更适合表达区域性数据。



Business Intelligence Workflow

1. **Problem Identification**
2. **Data Acquisition**
3. **Data Preparation**
4. **Data Analysis**
5. **Visualization & Reporting**

A problem statement问题陈述 that defines the problem we are trying to solve and who we are solving it for

Acquisition：theoretical issues，practical issues

ETL vs data preparation：

ETL：数据集成过程，用于从不同数据源中提取数据，将其转换为目标格式，并加载到数据仓库或数据库中。提取（Extract），转换（Transform），加载（Load）

数据准备：是将数据清理、整理和转换为适合特定分析或模型的格式的过程。

**MECE**（Mutually Exclusive, Collectively Exhaustive）

ME互斥：意味着划分的每一部分彼此独立、不重叠，每一部分只能属于一个类别，不会同时出现在多个类别中。

CE穷尽：指的是划分后的部分能够完全覆盖整个集合，不会遗漏任何内容。

**Drill down** 是指从数据的高层级或总览进入更详细、更具体的层次，逐步深入到更细分的数据中。这种操作通常用于探索细节、分析某个特定数据点或发现特定原因。

**Drill up** 是 drill down 的反向操作，即从详细层次回到更高层级或概览层次的数据。通过 drill up，用户可以从细节逐步抽象回更广泛的视角，看到总体趋势或宏观表现。

**MongoDB** 是一种流行的 **NoSQL 文档数据库**，以其灵活的数据模型和高扩展性而闻名。MongoDB 不使用传统的表格结构，而是采用 **文档存储**的方式，数据以类似 **JSON** 的格式（称为 BSON，二进制 JSON）存储

### 常用操作

创建：`db.createCollection("CollectionName")`;

- **插入数据**：`db.collection.insertOne()` 或 `db.collection.insertMany()` 用于插入单个或多个文档。
- **查询数据**：`db.collection.find()` 用于查找文档，支持条件查询、字段过滤、排序和分页。
- **更新数据**：`db.collection.updateOne()` 和 `db.collection.updateMany()` 用于更新一个或多个文档。
- **删除数据**：`db.collection.deleteOne()` 和 `db.collection.deleteMany()` 用于删除一个或多个文档。
- 不等式
  
       .find({attributeName: {$lt: 1}}): less than one;
    • .find({attributeName: {$lte: 1}}): less than or equal to one;
    • .find({attributeName: {$gt: 1}}): greater than one;
    • .find({attributeName: {$gte: 1}}): greater than or equal to one;
    • .find({attributeName: {$ne: 1}}): not equal to one;
    Inequalities in MongoDb QUeries