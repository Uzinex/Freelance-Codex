import { useParams } from 'react-router-dom';
import { useQuery } from '@apollo/client';
import { GET_PROJECT } from '../../api/projectsApi';

export default function ProjectDetail() {
  const { id } = useParams();
  const { data, loading } = useQuery(GET_PROJECT, {
    variables: { id: Number(id) },
  });

  if (loading) return <div>Loading...</div>;
  const project = data?.project;

  if (!project) return <div>Project not found</div>;

  return (
    <div className="space-y-2">
      <h1 className="text-xl font-bold">{project.title}</h1>
      <p>{project.description}</p>
      <p>Owner: {project.owner.username}</p>
      <p>
        Budget: {project.budgetMin} - {project.budgetMax}
      </p>
      <p>Status: {project.status}</p>
    </div>
  );
}
