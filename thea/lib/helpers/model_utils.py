def clear_models(models):
    """
    :type models: list[thea.lib.models.base_model.BaseModel]
    """
    for model in models:
        model.clear()