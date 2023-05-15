from osgeo import gdal

# Open the input GeoTIFF file
input_file = './test.tif'
dataset = gdal.Open(input_file)

# Get the size of the input raster
rows = dataset.RasterYSize
cols = dataset.RasterXSize

# Set the tile size to 1m x 1m
tile_size = 1

# Loop through each row and column, creating a new output GeoTIFF file for each tile
for i in range(0, rows, tile_size):
    for j in range(0, cols, tile_size):
        # Calculate the x and y offsets for this tile
        x_offset = j
        y_offset = i
        
        # Calculate the width and height of this tile
        width = min(tile_size, cols - j)
        height = min(tile_size, rows - i)
        
        # Create the output GeoTIFF file for this tile
        output_file = f'new_dataset/output_{x_offset}_{y_offset}.tif'
        driver = gdal.GetDriverByName('GTiff')
        dst_ds = driver.Create(output_file, width, height, dataset.RasterCount, dataset.GetRasterBand(1).DataType)
        
        # Copy the data from the input raster to the output raster
        dst_ds.SetGeoTransform((dataset.GetGeoTransform()[0] + x_offset * dataset.GetGeoTransform()[1], dataset.GetGeoTransform()[1], 0, dataset.GetGeoTransform()[3] + y_offset * dataset.GetGeoTransform()[5], 0, dataset.GetGeoTransform()[5]))
        dst_ds.SetProjection(dataset.GetProjection())
        for k in range(dataset.RasterCount):
            data = dataset.GetRasterBand(k+1).ReadAsArray(x_offset, y_offset, width, height)
            dst_ds.GetRasterBand(k+1).WriteArray(data)
        
        # Close the output GeoTIFF file
        dst_ds = None
