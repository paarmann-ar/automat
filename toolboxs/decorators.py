def singleton(class_):
    instance_dictionary = dict()

    def create_instance(*args, **kwargs):
        if class_ not in instance_dictionary:
            instance_dictionary[class_] = class_(*args, **kwargs)

        return instance_dictionary[class_]

    return create_instance
