"""Заготовки задач на NumPy."""

import numpy as np
from grader_contracts.numpy_tasks import (
    BinarizeInput, ChessInput, EllipseInput, MatrixInput, MatrixStatistics,
    MatrixVectorBatchInput, OneHotInput, RandomMatrixInput, RectangleInput,
    TimeSeriesInput, TimeSeriesStatistics,
)



def sum_prod(data: MatrixVectorBatchInput) -> np.ndarray:
    matrices, vectors = data.matrices, data.vectors
    s = np.zeros_like(vectors[0])
    for A, x in zip(matrices, vectors): 
        p = A @ x
        s = s + p
    return s
    raise NotImplementedError  # TODO


def binarize(data: BinarizeInput) -> np.ndarray:
    matrix, threshold = data.matrix, data.threshold
    res =[]
    for A in matrix:
        new = []
        for x in A:
            if x > threshold:
                new.append(1)
            else:
                new.append(0)
        res.append(new)
    return res
    raise NotImplementedError  # TODO


def unique_rows(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    res = []
    for A in matrix:
        u = np.unique(A)
        l = u.tolist()
        res.append(l)
    return res
    
    raise NotImplementedError  # TODO


def unique_columns(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    m = np.transpose(matrix)
    res = []
    for A in m:
        u = np.unique(A)
        l = u.tolist()
        res.append(l)
    return res
    raise NotImplementedError  # TODO


def matrix_statistics(data: RandomMatrixInput) -> MatrixStatistics:
    rows, columns, mean, std, seed = data.rows, data.columns, data.mean, data.std, data.seed
    np.random.seed(seed)
    matrix = np.random.normal(loc=mean, scale=std, size= (rows,columns)) 
    row_means = []
    row_vars = []
    for row in matrix:
        m_val = np.mean(row)
        v_val = np.var(row)
        row_means.append(m_val)
        row_vars.append(v_val)
    tran = np.transpose(matrix)
    col_means = []
    col_vars = []

    for col in transposed_matrix:
        m_val = np.mean(col)
        v_val = np.var(col)
        col_means.append(m_val)
        col_vars.append(v_val)
        
    row_means = np.array(row_means)
    row_vars = np.array(row_vars)
    col_means = np.array(col_means)
    col_vars = np.array(col_vars)
    
    return MatrixStatistics(matrix=matrix, row_means=row_means, col_means=col_means, row_vars=row_vars,col_vars=col_vars)

    raise NotImplementedError  # TODO


def chess(data: ChessInput) -> np.ndarray:
    rows, columns, first, second = data.rows, data.columns, data.first, data.secon
    m, n, a, b = data.m, data.n, data.a, data.b
    res = []
    for i in range(m):
        r = []
        for j in range(n):
            if (i + j) % 2 == 0:
                r.append(a)
            else:
                r.append(b)
        res.append(r)
    return np.array(res)
    raise NotImplementedError  # TODO


def draw_rectangle(data: RectangleInput) -> np.ndarray:
    width, height = data.width, data.height
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    
    y0 = image_height / 2.0
    x0 = image_width / 2.0
    
    y_min = y0 - height / 2.0
    y_max = y0 + height / 2.0
    x_min = x0 - width / 2.0
    x_max = x0 + width / 2.0
    img = []
    for y in range(image_height):
        row = []
        for x in range(image_width):
            if y_min <= y < y_max and x_min <= x < x_max:
                row.append(shape_color)       
            else:
                row.append(background_color)
        img.append(row)  
    return np.array(img)
    raise NotImplementedError  # TODO


def draw_ellipse(data: EllipseInput) -> np.ndarray:
    semi_axis_x, semi_axis_y = data.semi_axis_x, data.semi_axis_y
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color
    y0 = image_height / 2.0
    x0 = image_width / 2.0
    img = []
    for y in range(image_height):
        row = []
        for x in range(image_width):
            value = ((x - x0) ** 2) / (a ** 2) + ((y - y0) ** 2) / (b ** 2)
            if value <= 1.0:
                row.append(row.append(shape_color))
            else:
                row.append(background_color)     
                
    img.append(row)
    raise NotImplementedError  # TODO


def analyze_time_series(data: TimeSeriesInput) -> TimeSeriesStatistics:
    values, window = data.values, data.window
    n = len(values)
    expected_value = np.mean(values)                 
    range_value = np.max(values) - np.min(values)    
    std_value = np.std(values)
    
    local_maxima = []
    local_minima = []
    for i in range(1, n - 1):
        #локальный максимум
        if values[i] > values[i - 1] and values[i] > values[i + 1]:
            local_maxima.append(i)
        #лоfor i in range(n - window + 1):
            current_window = values[i : i + window]
            w_mean = np.mean(current_window)
            moving_average.append(w_mean)
        
    local_maxima = np.array(local_maxima)
    local_minima = np.array(local_minima)
    moving_average = np.array(moving_average)
    
    return TimeSeriesStatistics(
        expected_value=expected_value,
        range=range_value,
        std=std_value,
        local_maxima=local_maxima,
        local_minima=local_minima,
        moving_average=moving_average)
    ge = []
        for i in rangemes[i] < values[i - 1] and values[i] < values[i + 1]:
            local_minima.append(i)
        movingt
    if class_count is None:
        class_count = int(np.max(labels)) + 1
    res = []
    for val in labels:
        row = [0] * class_count
        row[val] = 1
        res.append(row)
    return np.array(res)average = []
        for i in rangementedError  # TODO


def one_hot(data: OneHotInput) -> np.ndarray:
    labels, class_count = data.labels, data.class_count
    raise NotImplementedError  # TODO
