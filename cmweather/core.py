import xarray as xr

def my_mean_func(data):
    """
    Computes mean of an xarray object.

    Parameters
    ----------
    data : xarray.DataArray, xarray.Dataset
        Input data

    Returns
    -------
    mean : xarray.DataArray, xarray.Dataset

    Raises
    ------
    TypeError
         if input data is not an xarray DataArray or xarray Dataset.
    """

    if isinstance(data, (xr.Dataset, xr.DataArray)):
        return data.mean()

    raise TypeError('input data must be xarray DataArray or xarray Dataset!')
