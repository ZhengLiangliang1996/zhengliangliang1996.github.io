---
title: "Cheatsheet: Pandas, Dataframe, (commonly used)"
date: "2021-11-13"
categories: 
  - "dl-ml-python"
---

**Input and Output**

- **pd.read\_pickle(path, compression='infer')**
    - 'infer' means detect compression from the following extensions: ‘.gz’, ‘.bz2’, ‘.zip’, or ‘.xz’
- **df.to\_pickle(path, compression='infer')**
    - Compression mode may be any of the following possible values: {‘infer’, ‘gzip’, ‘bz2’, ‘zip’, ‘xz’, None}. 
- **pd.read\_csv(path, sep=',', dtype=None)**
    - dtype: could specify for each column with {‘a’: np.float64, ‘b’: np.int32, ‘c’: ‘Int64’}
- **df.to\_csv(path, index=False)**
- **pd.read\_excel(path, _sheet\_name=0_, _header=0_, _dtype=None_, _engine=None)_**
    - header: int or None(if there is no header.)
    - dtype: could specify for each column with {‘a’: np.float64, ‘b’: np.int32, ‘c’: ‘Int64’}
    - engine:
        - “xlrd” supports old-style Excel files (.xls).
        - “openpyxl” supports newer Excel file formats.
        - “odf” supports OpenDocument file formats (.odf, .ods, .odt).
        - “pyxlsb” supports Binary Excel files.
- **dataframe.to\_excel(_path_, _sheet\_name='Sheet1'_)**
- **class** **pd.ExcelWriter(**_path_**,** _engine=None_**,** _date\_format=None_**,** _datetime\_format=None_**,** _mode='w'_)
    - mode{‘w’, ‘a’}, default ‘w’
    - The code below shows the example to use pd.ExcelWriter, you could go to xlsxWriter documentation to see more on how to use class [workbook](https://xlsxwriter.readthedocs.io/workbook.html) and class [worksheet](https://xlsxwriter.readthedocs.io/worksheet.html).

with pd.ExcelWriter(path, engine='xlsxwriter') as **ew**
    # Add a header format.
    workbook = ew.book
    header\_format = workbook.add\_format({
        'bold': **True**,
        'text\_wrap': **True**,
        'valign': 'top',
        'fg\_color': '#D7E4BC',
        'border': 1})
    # save dataframe to excel 
    df.to\_excel(**ew**, sheet\_name='Sheet1', header=true, index=False)
    # apply fmt
    worksheet = ew.sheets\['Sheet1'\]
    worksheet.set\_column(0, 0, width=15, cell\_format=header\_format)
    
    

**General Function**

- **Create dataframe**

[![](https://zhengliangliang.files.wordpress.com/2021/11/screenshot-2021-11-13-at-22.45.00.png?w=528)](https://zhengliangliang.files.wordpress.com/2021/11/screenshot-2021-11-13-at-22.45.00.png)

- **pd.melt(df, id\_vars=None, value\_vars=None, var\_name=None, value\_name='value')**
    - Gather Column into rows. (Inverse Operation of pivot)
    - **id\_vars: tuple, list, or ndarray**. Those columns that keep there position
    - **value\_vars:** **tuple, list, or ndarray** Column(s) to unpivot. If not specified, uses all columns that are not set as id\_vars
    - var\_name: name to use for the 'variable' column
    - value\_name: Name to use for the ‘value’ column

[![](https://zhengliangliang.files.wordpress.com/2021/11/screenshot-2021-11-13-at-09.34.42.png?w=532)](https://zhengliangliang.files.wordpress.com/2021/11/screenshot-2021-11-13-at-09.34.42.png)

- ****pd.merge(**_left_**,** _right_**,** _how='inner', on=None, left\_on=None, right\_on=None_**)****
    - merge 2 dataframe

[![](https://zhengliangliang.files.wordpress.com/2021/11/screenshot-2021-11-13-at-09.50.45.png?w=644)](https://zhengliangliang.files.wordpress.com/2021/11/screenshot-2021-11-13-at-09.50.45.png)

- **pd.concat(_objs_, _axis=0_, _join='outer'_, _ignore\_index=False_)**
    - **axis**{0/’index’, 1/’columns’}, default 0
    - The axis to concatenate along.**join**{‘inner’, ‘outer’}, default ‘outer’

[![](https://zhengliangliang.files.wordpress.com/2021/11/screenshot-2021-11-13-at-09.54.44.png?w=1024)](https://zhengliangliang.files.wordpress.com/2021/11/screenshot-2021-11-13-at-09.54.44.png)

- **pd.get\_dummies(_data_, _prefix=None_, _prefix\_sep='\_'_, _dummy\_na=False_, _columns=None_, _sparse=False_, _drop\_first=False_, _dtype=None_)**
    - Convert categorical variable into dummy/indicator variables
    - data:**dataarray-like, Series, or DataFrame**
- **pd.to\_datetime(**_arg_**,** _errors='raise'_**,** _dayfirst=False_**,** _yearfirst=False_**,** _utc=None_**,** _format=None_**,** _exact=True_**)**
    - arg: **_int, float, str, datetime, list, tuple, 1-d array, Series, DataFrame/dict-like_**
    - **errors**{‘ignore’, ‘raise’, ‘coerce’}, default ‘raise’
        - If ‘raise’, then invalid parsing will raise an exception.
        - If ‘coerce’, then invalid parsing will be set as NaT.
        - If ‘ignore’, then invalid parsing will return the input.
    - Format: The strftime to parse time, eg “%d/%m/%Y”, note that “%f” will parse all the way up to nanoseconds.
- **pd.eval(_expr_, _parser='pandas'_, _target=None_)**
    - Evaluate a Python expression as a string using various backends. (Not frequently used personally)
    - Exmaple: Add a new column using `pd.eval`:

pd.eval("double\_age = df.age \* 2", target=df)

**Dataframe**

**Sorting, reindexing, renaming**

- **df.sort\_values(_by_, _axis=0_, _ascending=True_, _inplace=False_, _kind='quicksort'_)**
    - **kind{‘quicksort’, ‘mergesort’, ‘heapsort’, ‘stable’}, default ‘quicksort’** (For DataFrames, this option is only applied when sorting on a single column or label.)
- **df.rename(mapper=None, index=None, columns=None, axis=None, copy=True, inplace=False, level=None, errors='ignore')**
- **df.reset\_index(**_level=None_**,** _drop=_True)
    - drop\[bool\]: Do not try to insert index into dataframe columns. This resets the index to the default integer index.

[![](https://zhengliangliang.files.wordpress.com/2021/11/screenshot-2021-11-13-at-22.59.12.png?w=582)](https://zhengliangliang.files.wordpress.com/2021/11/screenshot-2021-11-13-at-22.59.12.png)

**Subset Observation**: df.length, df.drop\_duplicates(_subset=None_), df\_sample, df\_nsmallest, df.head(n), df.tail(n), df.filter(), df.query()

- **df.filter(_items=None_, _like=None_, _regex=None_, _axis=None_)**

Select columns whose name matches regular expression regex.

[![](https://zhengliangliang.files.wordpress.com/2021/11/screenshot-2021-11-13-at-23.02.14.png?w=1024)](https://zhengliangliang.files.wordpress.com/2021/11/screenshot-2021-11-13-at-23.02.14.png)

**Summarize Data**

- **df.describe(_percentiles=None_, _include=None_, _exclude=None_, _datetime\_is\_numeric=False_)**
    - Generate descriptive statistics.
- **Series.nunique(_dropna=True_)**
    - Return number of unique elements in the object.
- **Series.value\_counts(**_normalize=False_**,** _sort=True_**,** _ascending=False_**,** _bins=None_**,** _dropna=True_**)**
    - Return a Series containing counts of unique values.

[![](https://zhengliangliang.files.wordpress.com/2021/11/screenshot-2021-11-13-at-23.10.35.png?w=730)](https://zhengliangliang.files.wordpress.com/2021/11/screenshot-2021-11-13-at-23.10.35.png)

**Handling Missing Data & Sanity Check Empty Data**

- **DataFrame.dropna(**_axis=0_**,** _how='any'_**,** _thresh=None_**,** _subset=None_**,** _inplace=False_**)**
    - Remove missing value rows(axis=0) or columns(axis=1)
- **DataFrame.fillna(**_value=None_**,** _method=None_**,** _axis=None_**,** _inplace=False_**,** _limit=None_**,** _downcast=None_**)**
- **print(df.isnull().sum().sum())**

**Group Data**

- **DataFrame.groupby(**_by=None_**,** _axis=0_**,** _level=None_**,** _as\_index=True_**,** _sort=True_**,** _group\_keys=True_**,** _squeeze=NoDefault.no\_default_**,** _observed=False_**,** _dropna=True_**)**
    - **by: mapping, function, label, or list of labels**
    - **dropna \[bool\], default True**

[![](https://zhengliangliang.files.wordpress.com/2021/11/screenshot-2021-11-13-at-23.24.57.png?w=1024)](https://zhengliangliang.files.wordpress.com/2021/11/screenshot-2021-11-13-at-23.24.57.png)

**Window Function**

- **df.rolling(**_window_**,** _min\_periods=None_**,** _center=False_**,** _win\_type=None_**,** _on=None_**,** _axis=0_**,** _closed=None_**,** _method='single'_**)**
    
    - window\[int\]: Size of the moving window. This is the number of observations used for calculating the statistic. Each window will be a fixed size.
    - min\_periods\[int\]: Minimum number of observations in window required to have a value 
    
    - win\_type: all possible win type can be found [here](https://docs.scipy.org/doc/scipy/reference/signal.windows.html#module-scipy.signal.windows)
- **df.expanding(_min\_periods=1_, _center=None_, _axis=0_, _method='single'_)**
    - Provide expanding transformations.

**Explode**

- **df.explode(_column_, _ignore\_index=False_)**
    - Transform each element of a list-like to a row, replicating index values.

**Reference**

1. [Dataframe cheatsheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
