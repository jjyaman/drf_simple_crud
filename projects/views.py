from .models import Project
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProjectSerializer


# List of the all Project in the DataBase
class ProjectsListAPIView(APIView):
    def get(self, request):
        projects = Project.objects.filter(status = True)
        projects_serializer = ProjectSerializer(projects, many = True)
        return Response(projects_serializer.data)
    

# Create a Project 
class ProjectsCreateAPIView(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# Consult for the PK or one register
class ProjectsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProjectSerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(status= True)
    

# Update the register of Project, only with the method put
class ProjectsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProjectSerializer

    # You can update records of projects that are disabled. 
    def get_queryset(self, pk= None):
        return self.get_serializer().Meta.model.objects.filter(id= pk).first()
    
    def put(self, request, pk = None):
        if self.get_queryset(pk):
            projects_serializer = self.serializer_class(self.get_queryset(pk), data= request.data)
            if projects_serializer.is_valid():
                projects_serializer.save()
                return Response({'message': 'Ambiente correctamente'}, status= status.HTTP_200_OK)
            return Response(projects_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Actualizado erroneamente'}, status= status.HTTP_400_BAD_REQUEST)
    


class ProjectsDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(status= True)
    
    def delete(self, request, pk= None):
        project = self.get_queryset().filter(id= pk).first()
        if project:
            project.status  = False
            project.save()
            return Response({'message': 'Eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No se pudo eliminar'}, status= status.HTTP_400_BAD_REQUEST)
    
    
    
    




